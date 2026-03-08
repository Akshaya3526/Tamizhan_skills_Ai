import streamlit as st
import pdfplumber
from openai import OpenAI

# Add your OpenAI API key
client = OpenAI(api_key="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")

st.title("Generative AI Resume Screening System")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Enter Job Description")

if uploaded_file is not None and job_desc:

    # Extract text from PDF
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    resume_text = text

    st.subheader("Resume Uploaded Successfully")

    prompt = f"""
    Analyze the resume and job description.

    Resume:
    {resume_text}

    Job Description:
    {job_desc}

    Do the following:
    1. Extract skills from resume
    2. Compare with job description
    3. Give matching skills
    4. Give match percentage
    5. Recommend Shortlist or Reject
    """

    if st.button("Analyze Resume"):

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are an AI resume screening assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        result = response.choices[0].message.content

        st.subheader("AI Analysis Result")
        st.write(result)
