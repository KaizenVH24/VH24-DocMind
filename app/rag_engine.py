from app.vector_store import VectorStore
from app.ollama_client import ask_ollama


class RAGEngine:
    def __init__(self):
        self.vs = VectorStore()

    def build_prompt(self, question, context_chunks):
        """
        Combine retrieved chunks + user question into a prompt
        """

        context_text = "\n\n".join([
            chunk.page_content for chunk, _ in context_chunks
        ])

        prompt = f"""
You are an AI assistant that answers strictly based on given context.

Context:
{context_text}

Question:
{question}

Instructions:
- ONLY use the information from the context
- Do NOT add your own knowledge
- If exact steps are listed, preserve them fully
- Do not skip any points
- If answer not found, say: "Not found in documents"

Answer:
"""
        return prompt

    def ask(self, question):
        # Step 1: retrieve relevant chunks
        results = self.vs.search(question, k=4)

        if not results:
            return "No relevant information found."

        # Step 2: build prompt
        prompt = self.build_prompt(question, results)

        # Step 3: call LLM
        answer = ask_ollama(prompt)

        return answer