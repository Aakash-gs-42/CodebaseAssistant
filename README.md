# CodebaseAssistant

Overview
This project combines a React Todo application with a powerful backend that leverages Retrieval-Augmented Generation (RAG) using Large Language Models (LLMs). Users can interactively ask questions about the project’s source code and documentation, and receive accurate, context-based answers sourced directly from the underlying files.

# What I Tried
- Developed a React-based TodoList Application

- Features add and list functionality.

- Code is structured with clear documentation and componentization.

- Built a Retrieval-Augmented Generation (RAG) Pipeline in Python

- Integrated LangChain and FAISS to manage document embeddings and vector-based search.

- Used ChatOllama (with the Mistral model) as the conversational AI backend.

- Implemented HuggingFace sentence-transformer embeddings for dense semantic retrieval.

- Processed Multiple Document Types

- Loaded and indexed both a project PDF and all relevant code files (.js, .jsx, .ts, .tsx, .json, .md) from the codebase.

- Used language-aware chunking (via LangChain’s JavaScript-specific splitter) to optimally split code for retrieval.


- Programmatically skipped non-relevant directories (such as node_modules, public) during code ingestion.

# What I Achieved

- Users can input natural language queries related to either documentation (PDF) or any part of the React codebase.

- The system retrieves relevant code/document chunks and formulates precise, contextually-grounded responses.

- Accurate Context Restriction

- The AI assistant only answers questions using the indexed context. If no answer is found, it responds transparently (“Not able to find in document”).

- Codebase and documentation are processed with chunking strategies appropriate for their content.

- Easy to extend: support for new file types or more advanced chunking can be added as the project evolves.

- All indexed documents retain metadata to identify their source file and location in the project. This enables source-backed answers and transparent retrieval.


# Key Technologies
- React: User interface for the Todo list.

- LangChain + FAISS: Semantic chunking, embedding, and retrieval.

- ChatOllama + Mistral: LLM-powered conversational answers.

- HuggingFace Embeddings: For robust vector search.

# Future Work
- Expand chunking to support more code languages and larger projects.

- Build a frontend UI for direct conversational interaction.

