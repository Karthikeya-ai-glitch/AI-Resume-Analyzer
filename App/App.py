import streamlit as st
import os
import json
import spacy
import pandas as pd
from pyresparser import ResumeParser

st.set_page_config(page_title="Lite Resume Analyzer", layout="wide")
st.title("🧠 Lite Resume Analyzer")

# Load job role data
with open("role_data.json", "r") as f:
    job_roles = json.load(f)

uploaded_file = st.file_uploader("Upload your Resume (PDF/DOCX)", type=["pdf", "docx"])

if uploaded_file:
    with open(os.path.join("Uploaded_Resumes", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

    data = ResumeParser(os.path.join("Uploaded_Resumes", uploaded_file.name)).get_extracted_data()
    if data:
        st.subheader("🔍 Extracted Resume Information")
        st.json(data)

        st.subheader("📌 Role-Based Recommendations")
        predicted_role = data.get("designation", "Unknown")
        matched = False
        for role in job_roles:
            if role.lower() in predicted_role.lower():
                st.markdown(f"### ⭐ Recommended Role: `{role}`")
                st.markdown("#### 📚 Suggested Skills:")
                st.markdown(", ".join(job_roles[role]["skills"]))
                st.markdown("#### 🎓 Suggested Courses:")
                for c in job_roles[role]["courses"]:
                    st.markdown(f"- {c}")
                matched = True
                break
        if not matched:
            st.warning("No direct match found for recommended job role.")
