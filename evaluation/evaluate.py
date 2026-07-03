import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.retriever import Retriever

retriever = Retriever()

test_questions = [
    "What is Artificial Intelligence?",
    "What is Machine Learning?"
]

for question in test_questions:
    print("=" * 60)
    print(f"Question: {question}")

    documents, metadata = retriever.retrieve(question)

    print(f"Retrieved {len(documents)} documents\n")

    for i, doc in enumerate(documents, 1):
        print(f"{i}. {doc[:200]}")
        print()
from app.retriever import Retriever

retriever = Retriever()

test_questions = [
    "What is Artificial Intelligence?",
    "What is Machine Learning?"
]

for question in test_questions:
    print("=" * 60)
    print(f"Question: {question}")

    documents, metadata = retriever.retrieve(question)

    print(f"Retrieved {len(documents)} documents\n")

    for i, doc in enumerate(documents, 1):
        print(f"{i}. {doc[:200]}")
        print()