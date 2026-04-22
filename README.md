🌙 Bed-Time Buddy — Intelligent RAG-Based Storytelling Chatbot
🧠 Overview

Bed-Time Buddy is a Retrieval-Augmented Generation (RAG) powered chatbot designed to deliver context-aware bedtime stories.

Retrieves relevant story segments from a curated dataset
Uses controlled prompting to ensure grounded responses
Generates safe, simple, and child-friendly storytelling answers
🎥 Demo



🖥️ Chat Interface

💬 Sample Interaction
User: Tell me a story about a brave rabbit

Bot: Once there was a small rabbit who lived near a quiet forest...
✨ Features
📚 RAG-based story generation
🔍 Semantic search using vector database
🧠 Context-aware responses
🎯 Controlled prompt to reduce hallucinations
⚡ Fast retrieval pipeline
💬 Interactive chat UI
🏗️ Architecture
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
📂 Project Structure
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
⚙️ How It Works
Load and process PDF stories
Split text into chunks
Convert chunks into embeddings
Store embeddings in Pinecone
Retrieve relevant chunks during query
Generate response using LLM
🛠️ Tech Stack
Python
Flask
LangChain
Pinecone
HuggingFace Embeddings
Ollama (phi3)
HTML + CSS
🚀 Setup Instructions
1. Clone Repository
git clone https://github.com/your-username/Bed-Time-Buddy.git
cd Bed-Time-Buddy
2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Add Environment Variables

Create a .env file:

PINECONE_API_KEY=your_api_key
PINECONE_INDEX=bed-time-buddy
5. Run Ollama Model
ollama run phi3
6. Create Vector Index
python store_index.py
7. Run Application
python app.py
8. Open in Browser
http://localhost:5000
🎯 Key Design Choices
RAG Architecture → reduces hallucinations
Pinecone → scalable vector search
MiniLM Embeddings → fast and efficient
Ollama (phi3) → local, cost-free inference
Strict Prompting → controlled outputs
⚠️ Known Issues
Merge conflict present in helper.py
Strict prompt may limit creativity
No conversation memory yet
🔮 Future Enhancements
🎙️ Text-to-Speech storytelling
🧠 Conversational memory
🧒 Personalized stories
🌍 Multi-language support
📱 Mobile-friendly UI
☁️ Cloud deployment
