# 🌙 Bed-Time Buddy — Intelligent RAG-Based Storytelling Chatbot

## 🧠 Overview

**Bed-Time Buddy** is a Retrieval-Augmented Generation (RAG) powered chatbot designed to deliver **context-aware bedtime stories**.

* Retrieves relevant story segments from a curated dataset
* Uses controlled prompting to ensure grounded responses
* Generates safe, simple, and child-friendly storytelling answers

---

## 🎥 Demo

<img width="1600" height="738" alt="image" src="https://github.com/user-attachments/assets/c2e0a284-c396-4ef5-a6c9-1dde91ba6fe4" />
<img width="1600" height="735" alt="image" src="https://github.com/user-attachments/assets/ead8454c-df0e-4fe7-a0e1-cd45d5c79deb" />
<img width="911" height="722" alt="image" src="https://github.com/user-attachments/assets/d9c97626-8b8c-4cf9-9d0a-e915394abac5" />


---

## 💬 Sample Interaction

**User:**

> Tell me a story about a brave rabbit

**Bot:**

> Once there was a small rabbit who lived near a quiet forest...

---

## ✨ Features

* 📚 RAG-based story generation
* 🔍 Semantic search using vector database
* 🧠 Context-aware responses
* 🎯 Controlled prompting to reduce hallucinations
* ⚡ Fast retrieval pipeline
* 💬 Interactive chat UI

---

## 🏗️ Architecture

```
User Query
   ↓
Embeddings (MiniLM)
   ↓
Pinecone Vector Search
   ↓
Top-K Chunks
   ↓
Prompt Engineering
   ↓
Ollama (phi3)
   ↓
Final Response
```

---

## 📂 Project Structure

```
Bed-Time-Buddy/
│
├── Data/
│   └── 365_bedtime_stories.pdf
│
├── Research/
│   └── trials.ipynb
│
├── src/
│   ├── chatbot.py
│   ├── helper.py
│   └── prompt.py
│
├── static/
│   ├── styles.css
│   └── *.png
│
├── templates/
│   └── chat.html
│
├── app.py
├── store_index.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. Load and process PDF stories
2. Split text into chunks
3. Convert chunks into embeddings
4. Store embeddings in Pinecone
5. Retrieve relevant chunks during query
6. Generate response using LLM

---

## 🛠️ Tech Stack

* Python
* Flask
* LangChain
* Pinecone
* HuggingFace Embeddings
* Ollama (phi3)
* HTML + CSS

---

## 🚀 Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/Bed-Time-Buddy.git
cd Bed-Time-Buddy
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Environment Variables

Create a `.env` file:

```env
PINECONE_API_KEY=your_api_key
PINECONE_INDEX=bed-time-buddy
```

### 5. Run Ollama Model

```bash
ollama run phi3
```

### 6. Create Vector Index

```bash
python store_index.py
```

### 7. Run Application

```bash
python app.py
```

### 8. Open in Browser

```
http://localhost:5000
```

---

## 🎯 Key Design Choices

* **RAG Architecture** → reduces hallucinations
* **Pinecone** → scalable vector search
* **MiniLM Embeddings** → fast and efficient
* **Ollama (phi3)** → local, cost-free inference
* **Strict Prompting** → controlled outputs

---

## ⚠️ Known Issues

* Merge conflict present in `helper.py`
* Strict prompt may limit creativity
* No conversation memory yet

---

## 🔮 Future Enhancements

* 🎙️ Text-to-Speech storytelling
* 🧠 Conversational memory
* 🧒 Personalized stories
* 🌍 Multi-language support
* 📱 Mobile-friendly UI
* ☁️ Cloud deployment

---

