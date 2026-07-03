from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    BSHTMLLoader,
)


class DocumentLoader:
    def load_documents(self, folder_path):
        documents = []

        folder = Path(folder_path)

        for file in folder.rglob("*"):
            suffix = file.suffix.lower()

            if suffix == ".pdf":
                loader = PyPDFLoader(str(file))
                documents.extend(loader.load())

            elif suffix in [".html", ".htm"]:
                loader = BSHTMLLoader(str(file))
                documents.extend(loader.load())

            elif suffix == ".md":
                loader = TextLoader(str(file))
                documents.extend(loader.load())

        return documents