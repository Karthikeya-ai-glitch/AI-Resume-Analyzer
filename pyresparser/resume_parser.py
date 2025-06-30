import re
import json

def parse_resume_text(text):
    name_match = re.search(r'Name[:\-]?\s*(.+)', text, re.IGNORECASE)
    email_match = re.search(r'\S+@\S+', text)
    phone_match = re.search(r'\+?\d[\d\-\s]{8,}\d', text)
    
    return {
        "name": name_match.group(1).strip() if name_match else "Not Found",
        "email": email_match.group(0) if email_match else "Not Found",
        "phone": phone_match.group(0) if phone_match else "Not Found"
    }

def extract_skills(text, known_skills):
    found_skills = []
    for skill in known_skills:
        if re.search(r'\b' + re.escape(skill.lower()) + r'\b', text.lower()):
            found_skills.append(skill)
    return list(set(found_skills))

def recommend_roles(skills, roles_json_path="role_data.json"):
    with open(roles_json_path, 'r', encoding='utf-8') as f:
        role_data = json.load(f)

    recommendations = []
    for role, data in role_data.items():
        required_skills = set(skill.lower() for skill in data["required_skills"])
        matching_skills = set(skill.lower() for skill in skills)
        match_count = len(required_skills & matching_skills)
        if match_count > 0:
            recommendations.append((role, match_count))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    return [role for role, _ in recommendations[:3]]  # top 3

def analyze_resume(txt_path, known_skills_path='skills.json'):
    with open(txt_path, 'r', encoding='utf-8') as f:
        text = f.read()

    with open(known_skills_path, 'r', encoding='utf-8') as f:
        known_skills = json.load(f)["skills"]

    basic_info = parse_resume_text(text)
    skills = extract_skills(text, known_skills)
    roles = recommend_roles(skills)

    return {
        "basic_info": basic_info,
        "skills_found": skills,
        "recommended_roles": roles
    }

