import spacy

# List of common technical skills - this can be expanded or loaded from a file
TECHNICAL_SKILLS = [
    "python", "java", "c++", "c#", "javascript", "typescript", "html", "css", "sql", "nosql",
    "react", "angular", "vue", "node.js", "django", "flask", "fastapi", "spring", "asp.net",
    "machine learning", "deep learning", "nlp", "computer vision", "tensorflow", "pytorch", "scikit-learn",
    "aws", "azure", "gcp", "docker", "kubernetes", "jenkins", "git", "linux", "agile", "scrum"
]

def extract_skills(text: str) -> list[str]:
    """
    Extracts skills from the given text based on a predefined list.
    """
    text = text.lower()
    found_skills = []
    
    # Simple keyword matching for now. Can be enhanced with spaCy EntityRuler or PhraseMatcher
    for skill in TECHNICAL_SKILLS:
        # Check if the skill exists as a whole word (simple heuristic)
        # Using a more robust regex or spaCy matcher would be better for production
        if skill in text:
             found_skills.append(skill)
             
    return list(set(found_skills))
