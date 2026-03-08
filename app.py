import streamlit as st
import pdfplumber

st.title("AI Resume Screening System")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Enter Job Description")

# Simple skill list
skills = ["python", "java", "sql", "machine learning", "data analysis", "excel", "communication"]

if uploaded_file is not None and job_desc:

    # Read PDF
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    resume_text = text.lower()
    job_text = job_desc.lower()

    matched_skills = []

    for skill in skills:
        if skill in resume_text and skill in job_text:
            matched_skills.append(skill)

    score = (len(matched_skills) / len(skills)) * 100

    st.subheader("Matching Skills")
    st.write(matched_skills)

    st.subheader("Resume Score")
    st.write(f"{score:.2f}% Match")
