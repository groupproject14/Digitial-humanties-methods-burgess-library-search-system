#!/usr/bin/env python
# coding: utf-8

# In[25]:


# import necessary modules
import json
import ollama
import chromadb


# In[26]:


# have python read the cleaned json data 

with open("/Users/alexgiles/Downloads/bookssample.json") as f:
    books = json.load(f)
# test that it worked sucesfully
print(books[1])  


# In[27]:


# add embeddings to the dataset
def embed_text(text):
    response = ollama.embeddings(
        model="nomic-embed-text",
        input= books
    )
    return response["embedding"]


# In[32]:


# establish datacollection with chromadb
client = chromadb.Client()
collection = client.get_or_create_collection(name="books")


# In[33]:


# assign each book in the sample with a vector, change '100' for a larger dataset

def format_book(book):
    return f"""{book}"""  

def get_embedding(text):
    return ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )["embedding"]

for i, book in enumerate(books[:100]):
    text = format_book(book)
    embedding = get_embedding(text)

    collection.add(
        documents=[text],
        embeddings=[embedding],
        metadatas=[book],
        ids=[str(i)]
    )

print("Sample assigned vector")


# In[34]:


# test by changing query and rerunning, changing n_results will affect the number of books recommended
query = "european fantasy"

query_embedding = get_embedding(query)

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=1
)

results["metadatas"][0]


# In[ ]:





# In[ ]:




