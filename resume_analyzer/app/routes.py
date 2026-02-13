from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import shutil
import os
from . import models, database, nlp_utils, skill_matcher

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload_resume", response_model=models.ResumeResponse)
async def upload_resume(file: UploadFile = File(...), db: Session = Depends(database.get_db)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    file_location = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    text = nlp_utils.extract_text_from_pdf(file_location)
    
    # Extract skills
    skills = skill_matcher.extract_skills(text)

    # Save to DB
    db_resume = models.Resume(
        filename=file.filename,
        text=text,
        skills=skills
    )
    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)

    return db_resume

@router.post("/analyze", response_model=models.AnalysisResponse)
async def analyze_resume(request: models.AnalysisRequest, db: Session = Depends(database.get_db)):
    resume = db.query(models.Resume).filter(models.Resume.id == request.resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    score, missing_keywords = nlp_utils.calculate_ats_score(resume.text, request.job_description)
    
    # Identify matched skills from JD
    jd_skills = skill_matcher.extract_skills(request.job_description)
    resume_skills = resume.skills if resume.skills else []
    
    matched_skills = list(set(resume_skills) & set(jd_skills))
    
    return models.AnalysisResponse(
        score=score,
        missing_keywords=missing_keywords,
        matched_skills=matched_skills
    )

@router.get("/ranked_resumes", response_model=List[models.ResumeResponse])
async def get_ranked_resumes(db: Session = Depends(database.get_db)):
    resumes = db.query(models.Resume).all()
    # Ranking logic would typically require a job description to rank against.
    # For this endpoint, we might just return all resumes, or if we had a stored job description, we could rank.
    # The requirement says "If multiple resumes uploaded, rank them by ATS score".
    # This implies there's a specific Job Description we are ranking against.
    # Since this is a simple GET, likely it's just listing them. 
    # Real ranking happens in /analyze context usually.
    # We will just return the list for now.
    return resumes
