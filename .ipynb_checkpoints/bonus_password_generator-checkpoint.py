"""
Bonus Challenge: Password Generator
Generate secure passwords with customizable options.
"""

import random
import string


def generate_password(length=12, use_uppercase=True, use_lowercase=True,
                     use_digits=True, use_special=True):
    """
    Generate a random password based on criteria.

    Args:
        length (int): Length of the password
        use_uppercase (bool): Include uppercase letters
        use_lowercase (bool): Include lowercase letters
        use_digits (bool): Include digits
        use_special (bool): Include special characters

    Returns:
        str: Generated password
    """
    characters = ""

    # TODO: Build character set based on parameters
    # if use_lowercase:
    #     characters += string.ascii_lowercase
    # etc.
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        return "Error: No character types selected!"

    password = []

    # TODO: Ensure at least one character from each selected type
    # This prevents passwords that don't meet the criteria
    if use_uppercase:
        password += random.choice(string.ascii_uppercase)
    if use_lowercase:
        password += random.choice(string.ascii_lowercase)
    if use_digits:
        length
    if use_special:
        password += random.choice(string.punctuation)
    # TODO: Fill the rest of the password randomly
    remaining = length- len(password)
    for i in range(remaining):
        password += random.choice(characters)
    # TODO: Shuffle the password list to randomize order
    password = list(password)
    random.shuffle(password)
    return ''.join(password)


def password_strength(password):
    """
    Rate password strength from 1-5.

    Args:
        password (str): Password to evaluate

    Returns:
        str: Strength rating
    """
    score = 0

    # TODO: Add points for different criteria
    # - Length >= 8: +1 point
    # - Length >= 12: +1 point
    # - Contains lowercase: +1 point
    # - Contains uppercase: +1 point
    # - Contains digits: +1 point
    if len(password) >=8:
        score +=1
    if len(password) >=12:
        score +=1
    for i in password:
        if i in string.ascii_lowercase:
            score+=1
            break
    for i in password:
        if i in string.ascii_uppercase:
            score+=1
            break
    for i in password:
        if i in string.digits:
            score+=1
            break
    
    strength = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
    return strength[min(score, 5)]


def main():
    """Main function to run the password generator."""
    print("Password Generator")
    print("-" * 30)

    # Get password length from user
    length_input = input("Password length (default 12): ").strip()
    length = int(length_input) if length_input else 12

    # Generate password
    password = generate_password(length)
    print(f"\nGenerated Password: {password}")
    print(f"Strength: {password_strength(password)}")

    # Generate alternative passwords
    print("\nAlternative passwords:")
    for i in range(3):
        alt_password = generate_password(length)
        print(f"{i+1}. {alt_password} ({password_strength(alt_password)})")


if __name__ == "__main__":
    main()