from app.rag_engine import RAGEngine

rag = RAGEngine()

question = "What are the phases of data science lifecycle?"

answer = rag.ask(question)

print("\nAnswer:\n")
print(answer)