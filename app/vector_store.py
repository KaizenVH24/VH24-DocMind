from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

import os


DB_DIR = "db"


class VectorStore:
    def __init__(self):
        # load embedding model once
        self.embedding = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        # create/load database
        self.db = Chroma(
            persist_directory=DB_DIR,
            embedding_function=self.embedding
        )

    def add_documents(self, chunks):
        if not chunks:
            return

        self.db.add_documents(chunks)
        print(f"Added {len(chunks)} chunks to DB")

    def search(self, query, k=4):
        results = self.db.similarity_search_with_score(query, k=k)
        return results

    def clear(self):
        """Safer clear — recreate DB instead of deleting live connection"""
        import shutil

        if os.path.exists(DB_DIR):
            self.db = None  # release reference
            shutil.rmtree(DB_DIR)

        # recreate fresh DB
        self.db = Chroma(
            persist_directory=DB_DIR,
            embedding_function=self.embedding
        )

        print("Database reset")