import time

from fastapi import FastAPI
from pydantic import BaseModel

from app.logger import logger
from app.retriever import Retriever
from app.llm import LLM

app = FastAPI(
    title="Cost Efficient RAG API",
    version="1.0.0",
    description="Low-cost RAG application using ChromaDB and Groq"
)

retriever = Retriever()
llm = LLM()


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Cost Efficient RAG API is running!",
        "docs": "/docs",
        "status": "success"
    }


@app.post("/query")
def query(request: QueryRequest):
    start_time = time.time()

    logger.info(f"Question: {request.question}")

    documents, metadata = retriever.retrieve(request.question)

    if not documents:
        logger.warning("No relevant context found.")

        latency = time.time() - start_time
        logger.info(f"Latency: {latency:.2f} seconds")

        return {
            "answer": "No relevant context found.",
            "sources": [],
            "latency_seconds": round(latency, 2)
        }

    context = "\n\n".join(documents)

    answer = llm.generate(request.question, context)

    latency = time.time() - start_time

    logger.info(f"Retrieved Chunks: {len(documents)}")
    logger.info(f"Latency: {latency:.2f} seconds")
    logger.info(f"Answer: {answer}")

    return {
        "question": request.question,
        "answer": answer,
        "sources": documents,
        "chunks_retrieved": len(documents),
        "latency_seconds": round(latency, 2)
    }