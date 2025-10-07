from fastapi import FastAPI
from rag.query_rag import ask_question
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  
    allow_credentials=True,
    allow_methods=["*"],   
    allow_headers=["*"], 
)
@app.get("/")
def root():
    return {"message":"GramAssist is running"}

@app.get("/ask")
def ask(q: str):
    answer = ask_question(q)
    return {"question":q, "answer":answer}