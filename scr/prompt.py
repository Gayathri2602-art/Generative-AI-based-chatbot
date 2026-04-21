from langchain.prompts import PromptTemplate

def get_prompt():
    template = """

Answer ONLY using the given context.

Rules:
- Do NOT create a story
- Do NOT add new characters
- Do NOT assume anything
- Answer in simple language, like you're telling a story to a child
- your response has to be more than 700 characters, but less than 1000 characters
- If exact answer not found, say: "I don't know"

Context:
{context}

Question:
{question}

"""

    return PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )