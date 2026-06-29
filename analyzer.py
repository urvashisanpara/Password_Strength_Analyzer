import re

def analyze_password(password, common_passwords):
    score = 0
    feedback = []

    # Length
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
    else:
        feedback.append("Password should be at least 8 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add uppercase letters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Add lowercase letters.")

    # Numbers
    if re.search(r"\d", password):
        score += 15
    else:
        feedback.append("Add numbers.")

    # Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 20
    else:
        feedback.append("Add special characters.")

    # Common Password
    if password.lower() in common_passwords:
        feedback.append("This is a common password.")
        score = max(score - 30, 0)

    # Strength
    if score >= 80:
        strength = "Very Strong"
    elif score >= 60:
        strength = "Strong"
    elif score >= 40:
        strength = "Medium"
    else:
        strength = "Weak"

    return score, strength, feedback
