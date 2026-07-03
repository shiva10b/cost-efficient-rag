import chromadb

from app.config import VECTOR_DB_PATH


class VectorStore:

    def __init__(self):
        self.client = chromadb.PersistentClient(path=VECTOR_DB_PATH)

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

    def add_documents(self, chunks, embedding_model):

        ids = []
        documents = []
        embeddings = []
        metadatas = []

        existing = set(self.collection.get()["ids"])

        for index, chunk in enumerate(chunks):

            doc_id = str(hash(chunk.page_content))

            if doc_id in existing:
                continue

            ids.append(doc_id)

            documents.append(chunk.page_content)

            embeddings.append(
                embedding_model.encode(chunk.page_content).tolist()
            )

            metadatas.append(chunk.metadata)

        if ids:
            self.collection.add(
                ids=ids,
                documents=documents,
                embeddings=embeddings,
                metadatas=metadatas
            )
def search(self, query_embedding, top_k, metadata_filter=None):

    query = {
        "query_embeddings": [query_embedding],
        "n_results": top_k
    }

    if metadata_filter:
        query["where"] = metadata_filter

    return self.collection.query(**query)

        