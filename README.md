# AI-Assisted PDF Chatbot using Retrieval-Augmented Generation (RAG)

## About the Project

This project is an AI-assisted chatbot that uses **Retrieval-Augmented Generation (RAG)** to answer questions based on user-provided PDF documents.

The main objective of this project was to gain hands-on experience with the core concepts behind RAG and understand how an LLM can generate more relevant, context-aware responses by retrieving information from external documents.

Instead of directly sending an entire document to the LLM, the application extracts the text, divides it into smaller chunks, converts those chunks into embeddings, and stores them in a vector database. When a user asks a question, the system performs semantic search to identify the most relevant chunks and passes the retrieved context along with the user's query to the LLM to generate an answer based on the provided document.

## How It Works – RAG Pipeline

The application follows these steps:

### 1. PDF Text Extraction
- **Technology:** PyPDF
- Extracts textual content from the PDF uploaded by the user.
- Makes the document content available for further processing.

### 2. Text Chunking
- **Technology:** Python
- Splits the extracted text into smaller, manageable chunks.
- Uses chunk size and overlap to preserve contextual information between consecutive chunks.

### 3. Embedding Generation
- **Technology:** Sentence Transformers (`all-MiniLM-L6-v2`)
- Converts each text chunk into a numerical vector representation.
- Captures the semantic meaning of the text, making similarity-based retrieval possible.

### 4. Vector Database
- **Technology:** FAISS (Facebook AI Similarity Search)
- Stores the generated embeddings in a vector index.
- Enables efficient similarity searches across the document chunks.

### 5. Semantic Search & Retrieval
- **Technology:** FAISS + Sentence Transformers
- Converts the user's question into an embedding using the same embedding model.
- Compares the query embedding with the stored document embeddings.
- Retrieves the top-k most relevant text chunks based on vector similarity.

### 6. Context-Aware Answer Generation
- **Technology:** Groq API + LLM
- Combines the retrieved text chunks with the user's original question.
- Passes both as context to the LLM through a structured prompt.
- Generates a natural-language response grounded in the provided document.

### 7. User Interface
- **Technology:** Streamlit
- Provides an interactive interface for uploading PDF documents and asking questions.
- Displays AI-generated responses and the retrieved source chunks for better transparency.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| PyPDF | PDF text extraction |
| Sentence Transformers | Text and query embeddings |
| all-MiniLM-L6-v2 | Embedding model |
| FAISS | Vector storage and similarity search |
| Groq API | LLM integration and answer generation |
| Streamlit | Interactive chatbot interface |

## Key Features

- Upload and interact with PDF documents.
- Automatic text extraction and chunking.
- Semantic search using vector embeddings.
- Retrieval of the most relevant document sections.
- Context-aware AI-generated answers.
- Display of retrieved text chunks as supporting sources.

## What I Learned

Through this project, I gained practical experience with:

- Understanding the complete RAG architecture.
- Extracting and preprocessing unstructured document data.
- Implementing text chunking and overlapping strategies.
- Generating and working with vector embeddings.
- Understanding vector databases and FAISS indexing.
- Implementing semantic similarity search.
- Connecting retrieved context with an LLM for grounded response generation.
- Building an end-to-end AI application using Python and Streamlit.

## Project Objective

This project was built as a hands-on learning exercise to understand how Retrieval-Augmented Generation works internally, rather than relying entirely on high-level frameworks such as LangChain.

It provided an opportunity to implement the fundamental RAG pipeline step by step and understand how document retrieval and LLM-based generation work together to produce context-aware answers.