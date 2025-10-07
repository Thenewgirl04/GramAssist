import os
import langchain 
from dotenv import load_dotenv
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings

load_dotenv()


raw_data_dirs = "./data/raw"
db_dir = "../db/faiss_index"

def load_docs():
    docs = []
    for file in os.listdir(raw_data_dirs):
        if file.endswith(".txt"):
            filepath = os.path.join(raw_data_dirs, file)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            docs.append(Document(
                page_content=text,
                metadata ={"source":file}
            ))
    return docs

def split_docs(docs):

    splitter = RecursiveCharacterTextSplitter (
        chunk_size = 500,
        chunk_overlap = 50
    )

    return splitter.split_documents(docs)

def create_faiss_index(chunks):
    embeddings = NVIDIAEmbeddings(model="nvidia/nv-embedqa-e5-v5")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(db_dir)
    print(f"[+] Saved FAISS index to {db_dir}")

if __name__=="__main__":
    raw_docs = load_docs()
    print(f"[+] Loaded {len(raw_docs)} raw docs")

    chunks = split_docs(raw_docs)
    print(f"[+] Split into {len(chunks)} chunks")

    create_faiss_index(chunks)

