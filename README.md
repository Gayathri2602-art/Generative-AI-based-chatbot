RAG Chatbot (Llama 2)

A Retrieval-Augmented Generation (RAG) chatbot built using LangChain, Llama 3.2, and Pinecone for semantic document retrieval and context-aware question answering.

This project demonstrates how to build a document-based AI assistant that retrieves relevant information from a knowledge source and generates grounded responses using a large language model.

----

🚀 Overview

This project builds a document-based AI assistant:

Documents are embedded and stored in Pinecone

Relevant content is retrieved based on user queries

Context is passed to Llama 2

The chatbot generates grounded responses

---

🛠️ Tech Stack

Python

LangChain

Flask

Llama 2

Pinecone

Sentence Transformers

---

📌 Features

🔍 Semantic search with Pinecone

🤖 Context-aware responses

📚 Document-based Q&A

🌐 Flask web interface

----

How It Works

User Query → Embeddings → Pinecone Retrieval → Llama 2 → Response
