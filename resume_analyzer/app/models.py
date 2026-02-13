from sqlalchemy import Column, Integer, String, Text, JSON
from .database import Base
from pydantic import BaseModel
from typing import List, Optional

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    text = Column(Text)
    email = Column(String, nullable=True)
    skills = Column(JSON)  # Storing list of skills as JSON
    extracted_data = Column(JSON) # Store other extracted info

class JobDescription(BaseModel):
    description: str

class AnalysisRequest(BaseModel):
    job_description: str
    resume_id: int

class AnalysisResponse(BaseModel):
    score: float
    missing_keywords: List[str]
    matched_skills: List[str]

class ResumeResponse(BaseModel):
    id: int
    filename: str
    skills: List[str]
    
    class Config:
        orm_mode = True
