# Digitial-humanties-methods-burgess-library-search-system
Here is my search system prototype for recommending books from a Southampton local library based on genre and themes. It was made using Python, Ollama LLM and published using Streamlit. The data was collected from southampton libraries using Instant Data Scaper and cleaned by me. 

Overview
This project is a semantic search application for books using Streamlit, Ollama, and ChromaDB. It returns relevant book recommendations based on themes and word connections.

Technologies:
Python, Streamlit, ChromaDB, Ollama

Setup:
Install dependencies:
pip install streamlit chromadb ollama

Pull embedding model:
ollama pull nomic-embed-text

Run the app:
streamlit run app10.py

Usage
Enter a search query to retrieve similar books from the dataset.

Notes
Requires Ollama running locally. Dataset is loaded from a JSON file.
