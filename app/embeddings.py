from sentence_transformers import SentenceTransformer

from app.config import EMBEDDING_MODEL


class EmbeddingModel:

    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)

    def get_model(self):
        return self.model