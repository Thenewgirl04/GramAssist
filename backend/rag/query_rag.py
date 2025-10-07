import os
from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA, NVIDIAEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import retrieval_qa
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain


load_dotenv()

def load_faiss_index():
    embeddings = NVIDIAEmbeddings(model="nvidia/nv-embedqa-e5-v5")
    vectorstore= FAISS.load_local("../db/faiss_index", embeddings, allow_dangerous_deserialization=True)
    return vectorstore

def create_rag_chain():
    vectorstore = load_faiss_index()
    retriever = vectorstore.as_retriever(search_kwargs={"k":3})
    llm = ChatNVIDIA(model="mistralai/mixtral-8x22b-instruct-v0.1")
    prompt_template = """You are GramAssist, an AI assistant for Grambling State University.
    Use the following context to answer the question concisely.

    Context: {context}
    Question: {input}
    Helpful Answer:"""
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    document_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, document_chain)

    return rag_chain

def ask_question(question):
    chain = create_rag_chain()
    response = chain.invoke({"input": question})
    return response["answer"]

if __name__ == "__main__":
    print(ask_question("When is the closing date for fall 2025?"))
