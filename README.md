# Project Atlas

Atlas is a local-first, AI-powered research and study assistant. It allows users to provide their own knowledge sources, ask questions, and receive grounded answers backed by explicit source citations.

## Current Status: v0.3.0

Atlas now features the Retrieval-Augmented Generation (RAG) scaffolding. It successfully connects the multi-document retrieval engine to a prompt generator, systematically structuring retrieved context, strict system instructions, and user queries to prepare for language model ingestion.

### Features
* **File Ingestion:** Reads UTF-8 encoded text files and handles missing/invalid files gracefully.
* **Text Chunking:** Segments documents into configurable word-count blocks.
* **Exact-Word Search:** Matches query words against document chunks and ranks them by relevance.
* **Multi-Document Pipeline:** Aggregates search results across an entire folder of documents.
* **Prompt Orchestration:** Isolates retrieval from formatting, enforcing strict citation rules and building deterministic, AI-ready prompt payloads.

## Project Structure
```text
Project-Atlas/
├── src/
│   └── atlas/
│       ├── analyzer.py
│       ├── chunker.py
│       ├── document_loader.py
│       ├── generator.py
│       ├── multipipeline.py
│       ├── pipeline.py
│       ├── rag_pipeline.py
│       ├── reader.py
│       └── search.py
└── tests/
    ├── testAnalyzer.py
    ├── testChunker.py
    ├── testDocumentLoader.py
    ├── testGenerator.py
    ├── testMultiPipeline.py
    ├── testPipeline.py
    ├── testRagPipeline.py
    ├── testReader.py
    └── testSearch.py