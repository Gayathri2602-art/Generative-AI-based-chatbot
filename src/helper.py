from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

# --- 1. Load PDFs ---
def load_pdf(data_path: str):
    loader = PyPDFDirectoryLoader(data_path)
    documents = loader.load()
    print(f"Loaded {len(documents)} pages")
    return documents


<<<<<<< HEAD
# --- 2. Split documents ---
def text_split(documents, chunk_size=500, chunk_overlap=50):  
=======
# --- 2. Split documents into smaller chunks ---
def text_split(documents, chunk_size=500, chunk_overlap=100):
    """
    Splits the loaded documents into smaller chunks for embedding.
    
    Args:
        documents (List[Document]): List of langchain Document objects.
        chunk_size (int): Max characters per chunk.
        chunk_overlap (int): Number of overlapping characters between chunks.
        
    Returns:
        List[Document]: List of chunked documents.
    """
>>>>>>> 141307d5c4b62d7edba76edf097cf56c88ea9894
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks")
    return chunks


# --- 3. Embeddings ---
def download_hugging_face_embeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
):
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    return embeddings