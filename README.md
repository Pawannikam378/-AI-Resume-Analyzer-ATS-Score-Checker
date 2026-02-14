# 🚀 AI Resume Analyzer — ATS Score Checker  

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![NLP](https://img.shields.io/badge/NLP-spaCy-orange)
![ML](https://img.shields.io/badge/ML-scikit--learn-yellow)
![Docker](https://img.shields.io/badge/Deployment-Docker-blue)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

</p>

An AI-powered Resume Analyzer that evaluates resumes against job descriptions and calculates an **ATS compatibility score** using Natural Language Processing and Machine Learning.

Built to simulate real-world Applicant Tracking Systems used by recruiters.

---

## 🌐 Live Demo

🔗 **Demo Link:** http://localhost:8000
📄 **API Docs:** `/docs` (Swagger UI)

---

## 📌 Problem Statement

Most companies use ATS (Applicant Tracking Systems) to automatically filter resumes before a recruiter ever sees them.

This project:
- Analyzes resume content
- Compares it with job descriptions
- Detects missing keywords
- Ranks candidates
- Provides actionable insights

---

## ✨ Features

### 📄 Resume Processing
- Upload PDF resumes
- Extract text using PyMuPDF
- Store data in SQLite

### 🧠 NLP Processing
- Tokenization
- Stopword removal
- Lemmatization (spaCy)
- Text normalization

### 📊 ATS Score Calculation
- TF-IDF vectorization
- Cosine Similarity
- Score normalized to percentage (0–100)

### 🔍 Skill Matching
- Predefined technical skill database
- Matched vs Missing skills
- Keyword gap detection

### 🏆 Resume Ranking
- Compare multiple resumes
- Rank based on ATS score

### 📑 API Ready
- RESTful endpoints
- Swagger documentation
- Modular architecture

---

## 🧠 ATS Scoring Algorithm

### Step 1: Text Extraction  
Resume → Extract text using PyMuPDF  

### Step 2: Preprocessing  
- Lowercasing  
- Removing stopwords  
- Lemmatization  

### Step 3: Vectorization  
TF-IDF converts text into numeric vectors.

### Step 4: Similarity Calculation  

```
Cosine Similarity = (A · B) / (||A|| ||B||)
```

Where:
- A = Resume vector  
- B = Job Description vector  

Final score = similarity × 100

---

## 🏗 System Architecture

```
User → FastAPI Backend → NLP Processing → ML Scoring → Database → Response
```

---

## 🛠 Tech Stack

| Layer | Technology |
|--------|------------|
| Backend | FastAPI |
| NLP | spaCy |
| ML | scikit-learn |
| PDF Parsing | PyMuPDF |
| Database | SQLite |
| Deployment | Docker |
| Testing | Pytest |

---

## 📂 Project Structure

```
resume_analyzer/
│── app/
│   │── main.py
│   │── routes.py
│   │── models.py
│   │── database.py
│   │── nlp_utils.py
│   │── skill_matcher.py
│
│── templates/
│── static/
│── tests/
│── requirements.txt
│── Dockerfile
│── README.md
│── .gitignore
```

---

## ⚙️ Local Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/ai-resume-analyzer.git
cd ai-resume-analyzer
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4️⃣ Run Server

```bash
uvicorn app.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 🐳 Docker Setup

### Build Image

```bash
docker build -t resume-analyzer .
```

### Run Container

```bash
docker run -p 8000:8000 resume-analyzer
```

---

## 📊 Example Output

| Metric | Result |
|--------|--------|
| ATS Score | 84% |
| Matched Skills | Python, SQL, ML |
| Missing Skills | Docker, Kubernetes |
| Rank | 2 / 6 |

---

## 🧪 Testing

```bash
pytest
```

---

## 📈 Performance Considerations

- Efficient vectorization using TF-IDF
- Modular architecture for scalability
- Ready for migration to PostgreSQL
- Can integrate BERT for semantic scoring

---

## 🚀 Future Enhancements

- JWT Authentication  
- Admin Dashboard  
- Keyword Heatmap Visualization  
- DOCX Support  
- BERT-based similarity  
- Cloud Deployment (AWS / Render)  
- SaaS Multi-User System  

---


## 💼 Why This Project Is Portfolio-Ready

This project demonstrates:

- Backend API Development  
- NLP Implementation  
- Machine Learning Integration  
- Database Design  
- Docker Deployment  
- Real-world business problem solving  

---

## 📜 License

MIT License

---

## 👤 Author

Your Name: Pawan Nikam
Final Year Engineering Student  
Focused on AI, Data Science, Data Analytics, and IOT Systems 
