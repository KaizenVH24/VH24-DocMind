from app.document_loader import ingest_file
from app.vector_store import VectorStore
import shutil
import os

# clear DB manually BEFORE loading
if os.path.exists("db"):
    shutil.rmtree("db")

# now start fresh
vs = VectorStore()

chunks = ingest_file("data/sample.txt")
vs.add_documents(chunks)

results = vs.search("What is AI?")

for doc, score in results:
    print("\nScore:", score)
    print(doc.page_content[:200])