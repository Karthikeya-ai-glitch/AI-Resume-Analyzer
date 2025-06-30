import json
import re

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_basic_info(text):
    name_match = re.search(r'Name[:\-]?\s*(.+)', text, re.IGNORECASE)
    email_match = re.search(r'\S+@\S+', text)
    phone_match = re.search(r'\+?\d[\d\-\s]{8,}\d', text)

    return {
        'name': name_match.group(1).strip() if name_match else "Not Found",
        'email': email_match.group(0) if email_match else "Not Found",
        'phone': phone_match.group(0) if phone_match else "Not Found"
    }

def extract_skills(text, known_skills):
    found_skills = []
    for skill in known_skills:
        if re.search(r'\b' + re.escape(skill.lower()) + r'\b', text.lower()):
            found_skills.append(skill)
    return list(set(found_skills))

def load_roles_from_json(json_path='role_data.json'):
    with open(json_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def recommend_roles(skills, roles_dict):
    role_scores = {}
    for role, data in roles_dict.items():
        required = set([s.lower() for s in data['required_skills']])
        score = len(required & set([s.lower() for s in skills]))
        role_scores[role] = score

    sorted_roles = sorted(role_scores.items(), key=lambda x: x[1], reverse=True)
    recommended = [role for role, score in sorted_roles if score > 0]
    return recommended[:3]  # top 3 matches

