# src/chatbot.py

import os
from dotenv import load_dotenv
<<<<<<< HEAD

from langchain_community.vectorstores import Pinecone as PineconeVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
=======
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
>>>>>>> 141307d5c4b62d7edba76edf097cf56c88ea9894
from langchain.chains import RetrievalQA

from src.prompt import get_prompt  

# ----------------------------
<<<<<<< HEAD
# 0. Load ENV
=======
# 0. Load ENV 
>>>>>>> 141307d5c4b62d7edba76edf097cf56c88ea9894
# ----------------------------
load_dotenv()

# ----------------------------
<<<<<<< HEAD
# 1. Config
=======
# 1. Config (Use ENV or fallback)
# ----------------------------
# CONFIG
>>>>>>> 141307d5c4b62d7edba76edf097cf56c88ea9894
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
<<<<<<< HEAD
def get_qa_chain(k=2):   
=======
def get_prompt():
    template = """
    You are a helpful and polite medical assistant. 

    CORE INSTRUCTIONS:
    1. GREETINGS: If the user greets you (e.g., "Hi", "Hello", "Good morning"), respond warmly with a greeting and ask how you can assist them today.
    2. GRATITUDE: If the user thanks you or says they found what they needed, respond politely (e.g., "I'm happy I could help! Please come back if you need further assistance.")
  
    4. ACCURACY: If the answer isn't explicitly in the Context, summarize the relevant parts but mention the textbook focuses on those specific areas. 
    5. LIMITATIONS: If the question is completely unrelated to the Context or general medical knowledge, politely state your focus.

    Context: {context}

    Question: {question}

    Helpful Answer:
    """
    return PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )
# ----------------------------
# 5. RAG QA Chain
# ----------------------------
def get_qa_chain(k=5):
>>>>>>> 141307d5c4b62d7edba76edf097cf56c88ea9894
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