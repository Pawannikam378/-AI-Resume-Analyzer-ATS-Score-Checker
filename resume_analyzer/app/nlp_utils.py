import fitz  # PyMuPDF
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading 'en_core_web_sm' model...")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts text from a PDF file using PyMuPDF.
    """
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def preprocess_text(text: str) -> str:
    """
    Preprocesses text using spaCy: lemmatization and stopword removal.
    """
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct and not token.is_space]
    return " ".join(tokens)

def calculate_ats_score(resume_text: str, job_description: str):
    """
    Calculates ATS score using TF-IDF and Cosine Similarity.
    Returns score (0-100) and missing keywords.
    """
    processed_resume = preprocess_text(resume_text)
    processed_jd = preprocess_text(job_description)
    
    documents = [processed_resume, processed_jd]
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(documents)
    
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    score = round(similarity_matrix[0][0] * 100, 2)
    
    # Identify missing keywords (simplified approach)
    feature_names = tfidf.get_feature_names_out()
    resume_vector = tfidf_matrix[0].toarray()[0]
    jd_vector = tfidf_matrix[1].toarray()[0]
    
    missing_keywords = []
    for i, term in enumerate(feature_names):
        if jd_vector[i] > 0 and resume_vector[i] == 0:
            missing_keywords.append(term)
            
    # Sort missing keywords by their importance in JD (tfidf score)
    # This requires a bit more logic if we want strictly sorted by importance, 
    # but for now returning the list is a good start.
    
    return score, missing_keywords
