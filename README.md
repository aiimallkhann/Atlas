# Project Atlas

**Version:** 0.4.0  
**Status:** Active Development

Project Atlas is a locally hosted Retrieval-Augmented Generation (RAG) application developed in Python. It enables users to index personal documents and query their contents through a command-line interface.

Atlas uses Ollama to generate document embeddings and produce responses with a locally running language model. Document processing, embedding generation, retrieval, and inference are performed on the user's machine, without requiring external AI APIs.

## Features

### Local Language Model Inference

Atlas uses [Ollama](https://ollama.com/) to run language models locally.

- **Generation:** Llama 3
- **Embeddings:** `nomic-embed-text`
- No external API keys are required.
- Documents and queries are processed locally through the configured Ollama instance.

### Separate Knowledge Stores

Atlas maintains separate vector stores for built-in and user-provided knowledge.

- `base_vector_store.json` stores the project's built-in knowledge.
- `user_vector_store.json` stores embeddings generated from user-provided documents.

The user-specific vector store is excluded from version control through `.gitignore`, preventing personal document data from being committed to the repository.

### Semantic Search

Atlas implements vector-based semantic retrieval using NumPy.

Document chunks are converted into numerical embeddings. At query time, Atlas generates an embedding for the user's question and compares it with the stored vectors using cosine similarity.

The most relevant chunks are selected and passed to the language model as contextual information.

### Sliding Window Chunking

Documents are divided into overlapping text chunks before embedding generation.

The overlap preserves contextual continuity between adjacent chunks and reduces the likelihood of losing information at chunk boundaries.

### Context-Aware Response Generation

Retrieved document chunks are incorporated into a prompt and supplied to Llama 3.

This allows the language model to generate responses using information retrieved from the available knowledge stores rather than relying exclusively on its pre-trained knowledge.

## Technology Stack

| Component | Technology | Purpose |
|---|---|---|
| Programming Language | Python 3.x | Application development |
| Local Model Runtime | Ollama | Local model execution |
| Generation Model | Llama 3 | Response generation |
| Embedding Model | nomic-embed-text | Text embedding generation |
| Numerical Computing | NumPy | Vector operations and similarity calculations |
| HTTP Communication | HTTPX | Communication with the local Ollama API |
| Data Storage | JSON | Persistent vector storage |

## Project Structure

```text
Project-Atlas/
│
├── src/
│   └── atlas/
│       ├── chunker.py           # Sliding-window text segmentation
│       ├── document_loader.py   # Discovery of input text files
│       ├── embedder.py          # Embedding generation
│       ├── llm_client.py        # Language model communication
│       ├── main.py              # Command-line application entry point
│       ├── multipipeline.py     # Coordination of multiple knowledge stores
│       ├── reader.py            # Document reading and text extraction
│       └── search.py            # Vector similarity search
│
├── base_vector_store.json       # Built-in knowledge store
├── .gitignore                  # Excludes local user data
├── requirements.txt             # Python dependencies
└── README.md
```

**Runtime-generated file:**

```text
user_vector_store.json
```

This file is generated locally when user documents are indexed. It is intentionally excluded from version control.

## Prerequisites

Before installing Atlas, ensure that the following are available:

- Python 3.x
- [Ollama](https://ollama.com/) installed and running
- Git

## Installation

### 1. Install the Required Models

Pull the models through Ollama:

```bash
ollama pull llama3
ollama pull nomic-embed-text
```

Ensure the Ollama service is running before launching Atlas.

### 2. Clone the Repository

```bash
git clone https://github.com/aiimallkhann/Project-Atlas.git
cd Project-Atlas
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

For an isolated development environment, create and activate a virtual environment before installing dependencies.

## Usage

Atlas currently provides an interactive command-line interface.

### 1. Configure the Python Path

From the project root, configure `PYTHONPATH` so Python can locate the application package.

**Windows PowerShell:**

```powershell
$env:PYTHONPATH = "src"
```

### 2. Launch Atlas

```bash
python src/atlas/main.py
```

## Application Workflow

The current CLI provides the following operations:

### Build Personal Knowledge

Select the document indexing option and provide a directory containing `.txt` files.

Atlas processes the documents through the following stages:

1. Discovers the input text files.
2. Reads and extracts their contents.
3. Splits the text into overlapping chunks.
4. Generates embeddings using `nomic-embed-text`.
5. Stores the resulting vectors in `user_vector_store.json`.

### Chat

Select the chat option to query the indexed knowledge.

Atlas performs the following operations:

1. Converts the user's query into an embedding.
2. Searches the available knowledge stores using cosine similarity.
3. Retrieves the most relevant document chunks.
4. Constructs a prompt containing the retrieved context and the user's question.
5. Sends the prompt to Llama 3 through Ollama.
6. Returns the generated response through the CLI.

## Development Status

Project Atlas is under active development. Version 0.4.0 represents the current implementation of its local document ingestion, embedding, vector retrieval, and language model integration components.

The architecture is being developed incrementally, with an emphasis on modularity, local execution, and maintainable Python code.