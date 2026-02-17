# Enterprise Document Retrieval System using FAISS and RAG
This system allows users to search enterprise documents using natural language, retrieve semantically relevant content from PDFs, view source documents and page references, explore an AI-ready knowledge retrieval architecture
A full local version also includes a Retrieval-Augmented Generation (RAG) layer using a local LLM.

The project implements a complete semantic search pipeline including:
1. Document ingestion
2. Text chunking
3. Embedding generation
4. FAISS vector indexing
5. Contextual retrieval
6. Source attribution

## Dataset
The system is built by training 30 enterprise grade documents of different domains like HR, IT, Legal and Security. This created over 200 text chunks in the further process.

## Features

1. Semantic search over enterprise documents
2. Multi-domain document support (HR, IT, Legal, Security)
3. Dense embeddings using Sentence Transformers
4. FAISS vector database for fast similarity search
5. Source attribution with document name & page number
6. Modular design for RAG integration
7. Retrieval evaluation using Recall@K

## Tech Stack
1. Python
2. FAISS
3. SentenceTransformers
4. Streamlit
5. FastAPI
6. GPT4All
7. pymupdf

## How the System Works
1. PDFs are ingested and text is extracted
2. Documents are split into chunks
3. Each chunk is converted into embeddings
4. FAISS builds a vector index for similarity search
5. User query is embedded
6. Top-K relevant chunks are retrieved
7. Sources are displayed with document references

## Evaluation Metrics Used
Recall@5: 0.40
Evaluated over 10 manually created queries across 4 domains. 

## Local Full RAG Version (Advanced)
The local version of this project includes:
1. Retrieval-Augmented Generation (RAG)
2. Local LLM integration (GPT4All)
3. FastAPI backend
4. Context-grounded answer generation

Due to large model size (2–4GB), this version is not deployed online but can be run locally.

## Future Improvements
1. Deploy full RAG version using cloud GPU
2. Add multi-document summarization
3. Integrate conversation memory
4. Support larger enterprise datasets
5. Add authentication & role-based access

## Installation and running locally

``` bash
git clone https://github.com/JambavanAbhiram/Enterprise-Document-Retrieval
cd Enterprise-Document-Retrieval
pip install -r requirements.txt
streamlit run app.py

