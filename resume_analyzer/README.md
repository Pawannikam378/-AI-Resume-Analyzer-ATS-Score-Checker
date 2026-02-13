# AI Resume Analyzer

A production-ready AI Resume Analyzer web application built with Python, FastAPI, and spaCy.

## Features

- **Resume Upload**: Upload PDF resumes and extract text.
- **Job Description Analysis**: Analyze job descriptions using NLP.
- **ATS Scoring**: Calculate resume relevance using TF-IDF and Cosine Similarity.
- **Skill Extraction**: Identify technical skills from resumes.
- **Resume Ranking**: Rank multiple resumes based on their match score.
- **Interactive UI**: Clean dashboard for easy interaction.

## Setup Instructions

### Local Development

1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Download spaCy model:
    ```bash
    python -m spacy download en_core_web_sm
    ```
4.  Run the application:
    ```bash
    uvicorn app.main:app --reload
    ```
5.  Open `http://localhost:8000` in your browser.

### Docker

1.  Build the image:
    ```bash
    docker build -t resume-analyzer .
    ```
2.  Run the container:
    ```bash
    docker run -p 8000:8000 resume-analyzer
    ```

## ATS Scoring

The ATS score is calculated using TF-IDF (Term Frequency-Inverse Document Frequency) vectors and Cosine Similarity.
1.  The job description and resume text are converted into TF-IDF vectors.
2.  Cosine similarity is computed between the two vectors.
3.  The result is a score between 0 and 100 representing how well the resume matches the job description.

## API Documentation

- `POST /upload_resume`: Upload a PDF resume.
- `POST /analyze`: Analyze a resume against a job description.
- `GET /ranked_resumes`: Get a list of ranked resumes.

Visit `/docs` for the interactive Swagger UI.



