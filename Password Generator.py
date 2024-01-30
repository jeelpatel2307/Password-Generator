import random
import string

def generate_password(length=12, include_digits=True, include_special_chars=True):
    """
    Generate a random password with the specified length and character types.

    Args:
    - length (int): Length of the password (default is 12).
    - include_digits (bool): Include digits (0-9) in the password (default is True).
    - include_special_chars (bool): Include special characters in the password (default is True).

    Returns:
    - str: Generated password.
    """
    # Define character sets based on user preferences
    letters = string.ascii_letters
    digits = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''

    # Combine character sets
    all_chars = letters + digits + special_chars

    # Ensure password length is at least 4 characters
    length = max(length, 4)

    # Generate a random password
    password = random.sample(letters, 2) + random.sample(digits, 2) + random.sample(special_chars, 2)
    remaining_length = length - 6  # subtracting 6 for the characters already chosen
    password += random.sample(all_chars, remaining_length)

    # Shuffle the password characters
    random.shuffle(password)

    # Convert the list of characters to a string
    password_str = ''.join(password)

    return password_str

if __name__ == "__main__":
    # Example: Generate a password with length 16, including digits and special characters
    password = generate_password(length=16, include_digits=True, include_special_chars=True)
    print(f"Generated Password: {password}")
