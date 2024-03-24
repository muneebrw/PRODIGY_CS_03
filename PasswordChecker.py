import string

def password_strength(password):
    score = 0

    # Check for length
    if len(password) < 8:
        score += 1

    # Check for uppercase letters
    if any(c.isupper() for c in password):
        score += 1

    # Check for lowercase letters
    if any(c.islower() for c in password):
        score += 1

    # Check for numbers
    if any(c.isdigit() for c in password):
        score += 1

    # Check for special characters
    if any(c in string.punctuation for c in password):
        score += 1

    # Return the score
    if score == 0:
        return "Very weak"
    elif score == 1:
        return "Weak"
    elif score == 2:
        return "Moderate"
    elif score == 3:
        return "Strong"
    else:
        return "Very strong"

if __name__ == "__main__":
    password = input("Enter a password: ")
    print(f"Password strength: {password_strength(password)}")