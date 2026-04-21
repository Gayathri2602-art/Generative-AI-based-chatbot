# src/chatbot.py

import os
from dotenv import load_dotenv

from langchain_community.vectorstores import Pinecone as PineconeVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

from src.prompt import get_prompt  

# ----------------------------
# 0. Load ENV
# ----------------------------
load_dotenv()

# ----------------------------
# 1. Config
# ----------------------------
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("PINECONE_INDEX", "bed-time-buddy")

if not PINECONE_API_KEY:
    raise ValueError("❌ PINECONE_API_KEY not found in .env")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# ----------------------------
# 2. Embeddings
# ----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ----------------------------
# 3. Load Pinecone Index
# ----------------------------
def init_pinecone():
    docsearch = PineconeVectorStore.from_existing_index(
        index_name=INDEX_NAME,
        embedding=embeddings
    )
    return docsearch

# ----------------------------
# 4. RAG QA Chain
# ----------------------------
def get_qa_chain(k=2):   
    docsearch = init_pinecone()

    retriever = docsearch.as_retriever(search_kwargs={"k": k})

    llm = Ollama(
        model="phi3",       
        temperature=0.3
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=False,   
        chain_type_kwargs={"prompt": get_prompt()}
    )

    return qa