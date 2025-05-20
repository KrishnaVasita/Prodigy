import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # Lowercase check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # Number check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add at least one digit (0-9).")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&* etc.).")

    # Determine strength
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, feedback

def main():
    print("🔐 Password Complexity Checker 🔐")
    password = input("Enter your password: ")

    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("\nSuggestions to improve:")
        for suggestion in feedback:
            print(" - " + suggestion)

if __name__ == "__main__":
    main()
