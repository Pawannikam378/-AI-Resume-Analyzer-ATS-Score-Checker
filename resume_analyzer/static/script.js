document.addEventListener('DOMContentLoaded', () => {
    const uploadForm = document.getElementById('uploadForm');
    const uploadStatus = document.getElementById('uploadStatus');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const jobDescriptionInput = document.getElementById('jobDescription');
    const resultsSection = document.getElementById('resultsSection');
    const scoreDisplay = document.getElementById('scoreDisplay');
    const matchedSkillsList = document.getElementById('matchedSkillsList');
    const missingKeywordsList = document.getElementById('missingKeywordsList');
    const resumeTableBody = document.querySelector('#resumeTable tbody');
    const currentResumeIdSpan = document.getElementById('currentResumeId');
    const loadingDiv = document.getElementById('loading');

    let currentResumeId = null;

    // Load existing resumes on startup
    loadResumes();

    uploadForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const fileInput = document.getElementById('resumeFile');
        if (fileInput.files.length === 0) return;

        const formData = new FormData();
        formData.append('file', fileInput.files[0]);

        uploadStatus.textContent = "Uploading...";

        try {
            const response = await fetch('/upload_resume', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.detail || "Upload failed");
            }

            const data = await response.json();
            uploadStatus.textContent = `Upload successful! ID: ${data.id}`;
            uploadStatus.style.color = "green";
            currentResumeId = data.id;

            // Refresh list
            loadResumes();

        } catch (error) {
            uploadStatus.textContent = `Error: ${error.message}`;
            uploadStatus.style.color = "red";
        }
    });

    analyzeBtn.addEventListener('click', async () => {
        const jd = jobDescriptionInput.value;
        if (!jd) {
            alert("Please enter a job description.");
            return;
        }
        if (!currentResumeId) {
            alert("Please upload or select a resume first.");
            return;
        }

        resultsSection.style.display = 'block';
        loadingDiv.classList.remove('hidden');
        scoreDisplay.textContent = '-';
        matchedSkillsList.innerHTML = '';
        missingKeywordsList.innerHTML = '';
        currentResumeIdSpan.textContent = currentResumeId;

        try {
            const response = await fetch('/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    job_description: jd,
                    resume_id: currentResumeId
                })
            });

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.detail || "Analysis failed");
            }

            const data = await response.json();

            scoreDisplay.textContent = `${data.score}%`;

            // Populate skills
            data.matched_skills.forEach(skill => {
                const li = document.createElement('li');
                li.textContent = skill;
                matchedSkillsList.appendChild(li);
            });
            if (data.matched_skills.length === 0) {
                matchedSkillsList.innerHTML = '<li>No specific skills matched</li>';
            }

            // Populate missing keywords
            data.missing_keywords.forEach(keyword => {
                const li = document.createElement('li');
                li.textContent = keyword;
                missingKeywordsList.appendChild(li);
            });
            if (data.missing_keywords.length === 0) {
                missingKeywordsList.innerHTML = '<li>None detected</li>';
            }

        } catch (error) {
            alert(`Analysis Error: ${error.message}`);
        } finally {
            loadingDiv.classList.add('hidden');
        }
    });

    async function loadResumes() {
        try {
            const response = await fetch('/ranked_resumes');
            const resumes = await response.json();

            resumeTableBody.innerHTML = '';
            resumes.forEach(resume => {
                const row = document.createElement('tr');

                // Skills formatting
                const skillsStr = resume.skills ? resume.skills.join(', ') : 'None extracted';

                row.innerHTML = `
                    <td>${resume.id}</td>
                    <td>${resume.filename}</td>
                    <td>${skillsStr.substring(0, 50)}${skillsStr.length > 50 ? '...' : ''}</td>
                    <td><button class="btn-small" onclick="selectResume(${resume.id})">Select</button></td>
                `;
                resumeTableBody.appendChild(row);
            });
        } catch (error) {
            console.error("Failed to load resumes:", error);
        }
    }

    // Make selectResume available globally
    window.selectResume = (id) => {
        currentResumeId = id;
        document.getElementById('currentResumeId').textContent = id;
        alert(`Resume ID ${id} selected for analysis.`);
        // Scroll to analysis section
        document.querySelector('.analysis-section').scrollIntoView({ behavior: 'smooth' });
    };
});
