# Digitial-humanties-methods-burgess-library-search-system
Here is my search system prototype for recommending books from a Southampton local library based on genre and themes. It was made using Python, Ollama LLM and published using Streamlit. The data was collected from Southampton libraries using Instant Data Scaper and cleaned by me. 

Overview:
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

Documents in the repository:
- LLM Search system raw code! - This is my first code version, it works in JupyterLab but does not include the user-friendly app function
- app10.py is the code including the app
- booksample.json is my 100-book sample dataset that the code has been tested on
- Complete_Dataset_Burgess_Library is a larger dataset from Southampton libraries containing 3619 books. It could be used to develop the project.
