# VH24-DocMind

VH24-DocMind is a local Retrieval-Augmented Generation (RAG) application that allows users to ask questions about their own documents. It processes uploaded files, retrieves relevant content using vector similarity, and generates answers using a locally running language model.

The system is designed to run entirely offline when used locally with Ollama. A cloud-compatible version is also included for demonstration purposes.

Project live - https://vh24-ai.streamlit.app/

---

## Overview

Traditional chatbots rely only on pre-trained knowledge, which often leads to generic or incorrect responses. This project takes a different approach by grounding answers in user-provided documents.

The workflow is straightforward:

* Documents are loaded and split into smaller chunks
* Each chunk is converted into embeddings
* Embeddings are stored in a vector database
* When a question is asked, the most relevant chunks are retrieved
* The language model generates an answer based on those chunks

This ensures that responses are contextual, relevant, and tied to actual data.

---

## Features

* Works fully offline using Ollama (local LLM)
* Supports PDF, text, and Markdown files
* Semantic search using embeddings (sentence-transformers)
* Persistent vector storage using ChromaDB
* Clean Streamlit interface for interaction
* Cloud deployment mode with fallback response
* Modular and easy-to-understand code structure

---

## Project Structure

```
VH24-DocMind/
│
├── app/
│   ├── document_loader.py     # File loading and chunking
│   ├── vector_store.py        # Embedding and retrieval logic
│   ├── rag_engine.py          # RAG pipeline
│   └── ollama_client.py       # Local / cloud model handling
│
├── data/                      # Sample documents
├── db/                        # Vector database (auto-created)
├── uploads/                   # Uploaded files (runtime)
│
├── main.py                    # Streamlit app
├── requirements.txt
└── README.md
```

---

## Setup (Local)

### 1. Clone the repository

```
git clone https://github.com/KaizenVH24/VH24-DocMind.git
cd VH24-DocMind
```

### 2. Create a virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Install and run Ollama

Download Ollama from the official website and start the service:

```
ollama serve
```

Pull a model:

```
ollama pull mistral
```

### 5. Run the application

```
streamlit run main.py
```

---

## Usage

1. Upload a document from the sidebar (PDF, TXT, or MD)
2. Wait for the file to be processed and indexed
3. Enter a question related to the document
4. View the generated answer based on retrieved context

---

## Cloud Deployment

The application is deployed on Streamlit Cloud for demonstration.

Since cloud environments do not support local Ollama instances, the deployed version runs in a fallback mode where the language model is disabled. The interface and document pipeline remain functional.

---

## Limitations

* Local model (Ollama) is not available in cloud deployment
* Large documents may increase processing time
* Scanned PDFs are not supported without OCR preprocessing
* Embedding model is optimized for English text

---

## Future Improvements

* Add support for external APIs (OpenAI or HuggingFace) for cloud inference
* Improve UI with chat history and streaming responses
* Add document source citations in the interface
* Introduce authentication and multi-user support

---

## Testing

The system was tested using a mix of factual, analytical, and out-of-context queries to evaluate retrieval quality and response accuracy.

## Sample Queries

* What are the types of machine learning?
* Explain the data science lifecycle
* What is Retrieval-Augmented Generation (RAG)?
* What are common failure modes in machine learning projects?


## Expected Behaviour

- Answers should be grounded in uploaded documents
- Responses should not rely on external knowledge
- Irrelevant questions should return a fallback message
- Retrieved context should align with the final answer


## Observations

* The model performs well on structured and factual queries
* Slight summarisation may occur when multiple chunks are retrieved
* Response quality depends on chunk size and overlap configuration

---


## Author

Vinay Hulsurkar aka VH24

GitHub: https://github.com/KaizenVH24

LinkedIn: https://linkedin.com/in/vinayhulsurkar

My Website: https://vinayhulsurkar.netlify.app/

---

## License

This project is open for learning and personal use.
