import os
from dotenv import load_dotenv

# Load all variables from the .env file
load_dotenv()

# ---------- API Keys ----------

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ---------- Embedding Model ----------

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "all-MiniLM-L6-v2"
)

# ---------- ChromaDB Storage Path ----------

VECTOR_DB_PATH = os.getenv(
    "VECTOR_DB_PATH",
    "./chroma_db"
)

# ---------- Chunking Configuration ----------

CHUNK_SIZE = int(
    os.getenv("CHUNK_SIZE", 500)
)

CHUNK_OVERLAP = int(
    os.getenv("CHUNK_OVERLAP", 100)
)

# ---------- Retrieval ----------

TOP_K = int(
    os.getenv("TOP_K", 5)
)