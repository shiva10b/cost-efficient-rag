from app.loader import DocumentLoader
from app.chunker import Chunker
from app.embeddings import EmbeddingModel
from app.vectorstore import VectorStore


def main():
    print("Loading documents...")

    loader = DocumentLoader()
    documents = loader.load_documents("data")

    print(f"Loaded {len(documents)} documents")

    print("Splitting documents into chunks...")

    chunker = Chunker()
    chunks = chunker.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    print("Loading embedding model...")

    embedding_model = EmbeddingModel().get_model()

    print("Saving vectors to ChromaDB...")

    vector_store = VectorStore()
    vector_store.add_documents(chunks, embedding_model)

    print("✅ Ingestion completed successfully!")


if __name__ == "__main__":
    main()