from app.document_loader import ingest_file

chunks = ingest_file("data/sample.txt")

for i, chunk in enumerate(chunks[:3]):
    print("\n--- Chunk", i, "---")
    print(chunk.page_content[:200])