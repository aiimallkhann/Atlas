# Atlas

Atlas is a Python project focused on document processing and search. The first version establishes a basic pipeline for reading a text document, analyzing its contents, splitting it into chunks, and finding relevant passages through keyword matching.

The long-term goal is to develop Atlas into a document research and learning tool that helps users explore their files, find evidence, and eventually ask questions about the material.

## v0.1.0

### Features

- Read a text document from a file path.
- Calculate text length, word count, and line count.
- Split text into word-based chunks.
- Search chunks using query keywords.
- Score and rank matching chunks.
- Combine reading, analysis, chunking, and search in one pipeline.
- Run the search through a command-line interface.

### Project Structure

```text
Atlas/
├── src/
│   └── atlas/
│       ├── __init__.py
│       ├── reader.py
│       ├── analyzer.py
│       ├── chunker.py
│       ├── search.py
│       ├── pipeline.py
│       └── main.py
├── tests/
│   └── testPipeline.py
└── README.md
```

### How It Works

`reader.py` reads the document. `analyzer.py` calculates basic statistics. `chunker.py` splits the text into smaller sections. `search.py` scores and ranks chunks against the query. `pipeline.py` connects these operations, and `main.py` provides the terminal interface.

The search method is keyword-based. It does not yet perform semantic search or generate answers.

### Requirements

- Python 3
- Git, if cloning the repository

The current pipeline uses Python's standard library.

### Run Atlas

From the repository root, run these commands in PowerShell:

```powershell
$env:PYTHONPATH = "src"
python -m atlas.main
```

Follow the prompts to enter a document path, a search query, and a chunk size.

### Run Tests

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
```

The pipeline tests cover missing files, valid files, empty files, invalid chunk sizes, and search ranking.

### Limitations

- Searches one document per operation.
- Uses keyword matching rather than semantic similarity.
- Returns matching text passages instead of generated answers.
- Is designed for text files; PDF, Word, and image processing are not included.
- Does not have a graphical user interface.

### Roadmap

**v0.2.0: Multi-document search**

- Discover text files inside a folder.
- Process and search multiple documents.
- Rank results across the collection.
- Identify the source document for each result.
- Expand automated test coverage.

**Future development**

The longer-term direction includes semantic retrieval, evidence-grounded question answering, support for additional document formats and images, and a user interface. Machine-learning models and PyTorch-based components may be introduced where they serve a clear purpose.

These are planned capabilities, not features of v0.1.0.

### Development Approach

Atlas is being built incrementally. Each stage focuses on understanding the underlying concepts, implementing a working component, and testing it before adding more complexity.

### License

No license has been specified for this version.
