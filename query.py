from app.retriever import Retriever
from app.llm import LLM

retriever = Retriever()
llm = LLM()

question = input("Ask a question: ")

documents, metadata = retriever.retrieve(question)

context = "\n\n".join(documents)

answer = llm.generate(question, context)

print("\nAnswer:\n")
print(answer)

print("\nSources:\n")

for i, doc in enumerate(documents, 1):
    print(f"{i}. {doc[:150]}...")