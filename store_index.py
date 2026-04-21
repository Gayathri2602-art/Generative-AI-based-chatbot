# store_index.py

import os
from dotenv import load_dotenv

from pinecone import Pinecone, ServerlessSpec
from langchain_community.vectorstores import Pinecone as PineconeVectorStore

from src.helper import load_pdf, text_split, download_hugging_face_embeddings

# ----------------------------
# Load ENV
# ----------------------------
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("PINECONE_INDEX", "bed-time-buddy")

if not PINECONE_API_KEY:
    raise ValueError("❌ PINECONE_API_KEY not found in .env")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# ----------------------------
# Upload Function
# ----------------------------
def upload_to_pinecone(data_path: str):

    print("📄 Loading PDFs...")
    documents = load_pdf(data_path)

    print("✂️ Splitting into chunks...")
    chunks = text_split(documents)

    print("🔍 Loading embeddings...")
    embeddings = download_hugging_face_embeddings()

    print("☁️ Connecting to Pinecone...")
    pc = Pinecone(api_key=PINECONE_API_KEY)

    existing_indexes = [i["name"] for i in pc.list_indexes()]

    # ✅ Create index if not exists
    if INDEX_NAME not in existing_indexes:
        print(f"📦 Creating index: {INDEX_NAME}")
        pc.create_index(
            name=INDEX_NAME,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )

    print("⬆️ Uploading to Pinecone...")

    PineconeVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        index_name=INDEX_NAME
    )

    print("✅ Upload complete!")


# ----------------------------
# Run Script
# ----------------------------
if __name__ == "__main__":
    upload_to_pinecone("data/")