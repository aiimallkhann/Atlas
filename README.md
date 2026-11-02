# Project Atlas

Atlas is a local-first, AI-powered research and study assistant. It allows users to provide their own knowledge sources, ask questions, and receive grounded answers backed by explicit source citations.

## Current Status: v0.2.0

Atlas currently supports multi-document text search. It can ingest a directory of `.txt` files, chunk the text, perform keyword searches, and return ranked results with exact source file attribution.

### Features
* **File Ingestion:** Reads UTF-8 encoded text files and handles missing/invalid files gracefully.
* **Text Chunking:** Segments documents into configurable word-count blocks.
* **Exact-Word Search:** Matches query words against document chunks and ranks them by relevance.
* **Multi-Document Pipeline:** Aggregates search results across an entire folder of documents.
* **Source Attribution:** Guarantees every returned text chunk is explicitly tied to its source filename.

## Project Structure
```text
Project-Atlas/
├── src/
│   └── atlas/
│       ├── analyzer.py
│       ├── chunker.py
│       ├── document_loader.py
│       ├── multipipeline.py
│       ├── pipeline.py
│       ├── reader.py
│       └── search.py
└── tests/
    ├── testAnalyzer.py
    ├── testChunker.py
    ├── testDocumentLoader.py
    ├── testMultiPipeline.py
    ├── testPipeline.py
    ├── testReader.py
    └── testSearch.py