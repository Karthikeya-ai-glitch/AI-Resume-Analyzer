# 🧠 Lite Resume Analyzer
A simple, local tool that extracts information from resumes and recommends job roles, skills, and courses.

## ✅ Features
- Upload resumes (PDF/DOCX)
- Auto extract details like name, skills, email, etc.
- Match with roles and suggest skills + courses

## 🚀 Getting Started
```bash
git clone https://github.com/karthikeya-ai-glitch/AI-Resume-Analyzer.git
cd App
python -m venv venvapp
venvapp\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run App.py
```

## 🔍 Supported Roles
- Data Scientist
- Product Manager
- AI/ML Engineer
... and more in `role_data.json`

## 📄 Author
Made with 💙 by [Karthikeya Nari](https://github.com/karthikeya-ai-glitch)
