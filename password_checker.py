import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/\\|`~]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")

    print("\nPassword Strength Score:", strength, "/ 5")
    if strength == 5:
        print("Status: Strong password ✅")
    else:
        print("Status: Weak password ❌")
        print("Suggestions:")
        for f in feedback:
            print("-", f)

if __name__ == "__main__":
    user_password = input("Enter a password to check: ")
    check_password_strength(user_password)
