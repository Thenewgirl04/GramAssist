# 📚 GramAssist

**An AI-Powered Campus Assistant for Grambling State University**

---

## 🚀 Overview

**GramAssist** is a personal project designed to help Grambling State University students, staff, and visitors access accurate, AI-driven answers about university information. Built with a full RAG (Retrieval-Augmented Generation) pipeline, GramAssist scrapes and indexes official GSU web content, retrieves relevant information using FAISS embeddings, and generates natural-language responses with NVIDIA NIM models.

---

## 🧠 Tech Stack

### **Backend**

* **FastAPI** — for building REST endpoints (`/ask`) and serving the RAG pipeline.
* **LangChain** — for connecting the LLM with the vector store and handling prompt chaining.
* **NVIDIA NIM Endpoints** — for embedding and text-generation models.
* **FAISS** — for efficient vector similarity search and document retrieval.
* **BeautifulSoup4 + Requests** — for web scraping and document extraction.
* **Python-dotenv** — for environment variable management.

### **Frontend**

* **Next.js (React)** — for the web-based chat interface.
* **TailwindCSS** — for responsive, GSU-themed styling.
* **Framer Motion** — for chat bubble animations and smooth transitions.

### **Storage**

* **FAISS Local Index** — for vector embeddings storage.
* **Text/JSON** — for storing scraped and processed data.
*(Planned)* **PostgreSQL with pgvector** — for scalability.
*(Future)* **Render / Railway / Heroku** — for backend deployment.
*(Future)* **Vercel** — for frontend hosting.
---

## ⚙️ Setup Instructions

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/Thenewgirl04/GramAssist.git
cd GramAssist
```

### **2️⃣ Backend Setup**

```bash
cd backend
python -m venv venv
source venv/bin/activate   # (use venv\Scripts\activate on Windows)
pip install -r requirements.txt
```

Create a `.env` file in the `backend` folder:

```env
NVIDIA_API_KEY=your_api_key_here
```

Run the backend:

```bash
uvicorn main:app --reload
```

Visit the docs at: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

### **3️⃣ Frontend Setup**

```bash
cd frontend
npm install
npm run dev
```

Access the app at: **[http://localhost:3000](http://localhost:3000)**

---

## 💬 Features

* 🧠 **RAG-based QA**: Combines context retrieval + generative responses.
* 🎓 **GSU Data Source**: Uses scraped content from Grambling State’s website.
* 💬 **Chat Interface**: Real-time, animated Q&A experience with Tailwind + Framer Motion.
* 🔒 **Environment Security**: `.env` setup with proper `.gitignore` protection.

---

## 📈 Future Improvements

* 🗂️ Add admin dashboard for uploading new knowledge sources.
* 💾 Store conversation history in a database.
* 🔍 Integrate authentication (student vs. faculty).
* ☁️ Deploy fully on Vercel + Render for public access.

---

## 🧑🏽‍💻 Author

**Chinwendu Onwuka**
Computer Science Major @ Grambling State University
📧 [theresaonwuka15@gmail.com](mailto:theresaonwuka15@gmail.com)
🔗 [LinkedIn](https://linkedin.com/in/chinwendu-onwuka) | [GitHub](https://github.com/Thenewgirl04)

---

## 🏛️ License

This project is for **educational and personal portfolio purposes**.
