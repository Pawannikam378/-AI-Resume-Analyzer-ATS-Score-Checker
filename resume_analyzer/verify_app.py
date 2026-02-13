import requests
import fitz  # PyMuPDF

# 1. Create a dummy PDF
doc = fitz.open()
page = doc.new_page()
text = "Experienced Python Developer with skills in Django, Flask, and FastAPI. Looking for a backend role."
page.insert_text((50, 50), text)
pdf_filename = "test_resume.pdf"
doc.save(pdf_filename)
doc.close()

print(f"Created {pdf_filename}")

# 2. Upload Resume
url = "http://localhost:8000"
files = {'file': open(pdf_filename, 'rb')}
try:
    response = requests.post(f"{url}/upload_resume", files=files)
    if response.status_code == 200:
        resume_data = response.json()
        print("Upload successful:", resume_data)
        resume_id = resume_data['id']
    else:
        print("Upload failed:", response.text)
        exit(1)
except Exception as e:
    print(f"Error connecting to server: {e}")
    exit(1)

# 3. Analyze Resume
job_description = "We are looking for a Python Developer with experience in FastAPI and Django."
payload = {
    "job_description": job_description,
    "resume_id": resume_id
}

response = requests.post(f"{url}/analyze", json=payload)
if response.status_code == 200:
    analysis = response.json()
    print("Analysis results:", analysis)
else:
    print("Analysis failed:", response.text)

# 4. Get Ranked Resumes (List)
response = requests.get(f"{url}/ranked_resumes")
if response.status_code == 200:
    resumes = response.json()
    print(f"Total resumes: {len(resumes)}")
else:
    print("Failed to get resumes:", response.text)
