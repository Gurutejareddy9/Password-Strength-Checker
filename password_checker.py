def evaluate_password_strength(password: str) -> int:
    """
    Evaluate the strength of a given password.

    :param password: The password to evaluate
    :return: A strength score (0-5)
    """
    score = 0

    # Check for password length
    if len(password) >= 12:
        score += 1

    # Verify the presence of:
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(not char.isalnum() for char in password):
        score += 1

    # Bonus point for exceptional passwords
    if len(password) >= 20 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and any(not char.isalnum() for char in password):
        score += 1

    return score


def main():
    password = input("Enter a password to evaluate its strength: ")
    strength_score = evaluate_password_strength(password)

    print(f"Password Strength Score: {strength_score}/5")
    if strength_score < 3:
        print("Weak password. Consider improving its strength!")
    elif strength_score < 5:
        print("Medium-strength password. Good, but could be better!")
    else:
        print("Strong password! Well done!")


if __name__ == "__main__":
    main()
