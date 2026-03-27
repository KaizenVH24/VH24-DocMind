import os
from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_text_file(file_path):
    """Load a text/markdown file"""
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    return [Document(
        page_content=content,
        metadata={"source": file_path}
    )]


def load_pdf(file_path):
    """Load PDF file"""
    from langchain_community.document_loaders import PyPDFLoader

    loader = PyPDFLoader(file_path)
    return loader.load()


def load_file(file_path):
    """Auto-detect file type"""
    ext = Path(file_path).suffix.lower()

    if ext == ".pdf":
        return load_pdf(file_path)
    elif ext in [".txt", ".md"]:
        return load_text_file(file_path)
    else:
        raise ValueError(f"Unsupported file: {ext}")


def chunk_documents(documents):
    """
    Break documents into smaller pieces.
    Overlap helps maintain context between chunks.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(documents)

    # Add chunk index (useful later for citations)
    for i, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = i

    return chunks


def ingest_file(file_path):
    docs = load_file(file_path)
    chunks = chunk_documents(docs)

    print(f"Loaded {len(docs)} docs → {len(chunks)} chunks")

    return chunks