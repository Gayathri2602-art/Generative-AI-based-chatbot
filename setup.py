from setuptools import find_packages, setup

setup(
    name="rag_chatbot",
    version="0.1.0",
    author="Gayathri V.R",   # 👈 update if needed
    packages=find_packages(),
    install_requires=[
        "flask",
        "langchain",
        "langchain-community",
        "pinecone",
        "sentence-transformers",
        "python-dotenv",
        "pypdf",
        "tqdm",
        "ollama"
    ],
)