#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import json
import ollama
import chromadb


# In[ ]:


# Load data from json

with open("/Users/alexgiles/Downloads/bookssample.json") as f:
    books = json.load(f)


# In[ ]:


# ChromaDB setup to store the data

client = chromadb.Client()
collection = client.get_or_create_collection(name="books")


# In[ ]:


# Embedding to assign vectors to each book

def get_embedding(text):
    return ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )["embedding"]


# In[ ]:


# Build DB once (cached so that the data is not changed when rerunning)

@st.cache_resource
def build_db():
    for i, book in enumerate(books[:100]): 
        text = f"""
        Title: {book['Title']}
        Author: {book['Author']}
        Description: {book['Description']}
        Genre: {book['Genre']}
        Fiction?: {book['Fiction?']}
        """

        embedding = get_embedding(text)

        collection.add(
            documents=[text],
            embeddings=[embedding],
            metadatas=[book],
            ids=[str(i)]
        )

    return collection


collection = build_db()


# In[ ]:


# building an application with Streamlit to present the prototype

st.title("Burgess Road Library Search Engine")

query = st.text_input("What kind of book would you like? (e.g. biography , war history, romance):")

if query:
    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )
#formatting results
    st.subheader("Results")

    for i, meta in enumerate(results["metadatas"][0]):
        st.markdown(f"### {i+1}. {meta['Title']}")
        st.write("**Author:**", meta["Author"])
        st.write("**Genre:**", meta["Genre"])
        st.write("**Description:**", meta["Description"])
        st.write("---")

