# Cost-Efficient RAG Application

## Overview

This project is a Retrieval-Augmented Generation (RAG) application built as part of the Applied AI / ML Engineering Take-Home Assignment.

The application allows users to ask questions over a collection of PDF, HTML and Markdown documents using semantic search powered by ChromaDB and Sentence Transformers. Retrieved document chunks are provided to a Large Language Model (Groq Llama 3.3) to generate grounded answers.

---

## Features

* PDF, HTML and Markdown document ingestion
* Automatic document chunking
* Sentence Transformer embeddings
* ChromaDB persistent vector database
* Idempotent ingestion (duplicate chunks are skipped)
* Metadata storage
* Configurable Top-K retrieval
* Grounded answer generation using Groq LLM
* FastAPI REST API
* Swagger API documentation
* Query logging
* Latency measurement

---

## Project Structure

```
cost-efficient-rag/
│
├── app/
│   ├── chunker.py
│   ├── config.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── loader.py
│   ├── logger.py
│   ├── retriever.py
│   └── vectorstore.py
│
├── chroma_db/
├── data/
├── evaluation/
├── logs/
├── ingest.py
├── main.py
├── query.py
└── README.md
```

---

## Technologies Used

* Python 3.11
* FastAPI
* ChromaDB
* Sentence Transformers
* LangChain
* Groq API
* Hugging Face
* Uvicorn

---

## Installation

Create a virtual environment.

```
python3.11 -m venv venv
```

Activate it.

```
source venv/bin/activate
```

Install dependencies.

```
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```
GROQ_API_KEY=YOUR_API_KEY
VECTOR_DB_PATH=./chroma_db
EMBEDDING_MODEL=all-MiniLM-L6-v2
CHUNK_SIZE=500
CHUNK_OVERLAP=100
TOP_K=5
```

---

## Ingest Documents

Place your documents inside the `data/` folder.

Run:

```
python ingest.py
```

---

## Start API

```
uvicorn main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Example Request

```
POST /query
```

```
{
    "question":"What is Artificial Intelligence?"
}
```

---

## Example Response

```
{
    "question":"What is Artificial Intelligence?",
    "answer":"Artificial Intelligence enables computers to perform tasks requiring human intelligence.",
    "chunks_retrieved":2,
    "latency_seconds":0.63
}
```

---

## Evaluation

The retrieval pipeline was tested using multiple natural language questions against the indexed corpus.

Evaluation included:

* Top-K Retrieval
* Retrieval Accuracy
* Semantic Search Quality
* Latency Measurement

---

## Cost Discussion

ChromaDB is used as the vector database because it is free, lightweight and suitable for small to medium sized deployments.

Compared to managed vector databases, ChromaDB significantly reduces infrastructure cost while maintaining good retrieval quality.

Managed vector databases become preferable for:

* High availability
* Multi-node deployments
* Enterprise scale
* Automatic backups
* Managed scaling

---

## Future Improvements

* Hybrid Retrieval (BM25 + Vector Search)
* Metadata Filtering
* Reranking
* Streaming Responses
* Better Evaluation Metrics
* Authentication
* Docker Deployment

---

## Author

Snehil Shukla
