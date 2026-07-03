from app.vectorstore import VectorStore
from app.embeddings import EmbeddingModel
from app.config import TOP_K


class Retriever:

    def __init__(self):
        self.vector_store = VectorStore()
        self.embedding_model = EmbeddingModel().get_model()

    def retrieve(self, query, top_k=TOP_K, metadata_filter=None):

        query_embedding = self.embedding_model.encode(query).tolist()

        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k,
            metadata_filter=metadata_filter
        )

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        return documents, metadatas