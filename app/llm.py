import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class LLM:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate(self, question, context):
        prompt = f"""
You are a helpful AI assistant.

Answer ONLY from the provided context.

If the answer is not present, reply:
"I could not find relevant information in the provided documents."

Context:
{context}

Question:
{question}
"""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content