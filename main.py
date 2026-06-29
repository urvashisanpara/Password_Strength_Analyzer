from analyzer import analyze_password
from generator import generate_password
from database import password_exists, save_password

with open("common_passwords.txt") as f:
    common_passwords = set(line.strip().lower() for line in f)

print("="*50)
print(" PASSWORD STRENGTH ANALYZER ")
print("="*50)

password = input("Enter Password: ")

if password_exists(password):
    print("\n❌ Password has already been used.")
else:
    score, strength, feedback = analyze_password(password, common_passwords)

    print("\nStrength :", strength)
    print("Score :", score, "/100")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print("-", item)

    if strength != "Very Strong":
        print("\nSuggested Strong Password:")
        print(generate_password())

    save_password(password)

print("\nFinished.")
