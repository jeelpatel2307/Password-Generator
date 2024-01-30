# Password Generator

The Password Generator is a simple Python script that generates random passwords with customizable length and character types.

## How It Works

The script defines a `generate_password` function that takes three optional parameters:

- **length (int):** Length of the password (default is 12).
- **include_digits (bool):** Include digits (0-9) in the password (default is True).
- **include_special_chars (bool):** Include special characters in the password (default is True).

The function creates character sets based on user preferences, combines them, and shuffles the characters to form the final password.

## Usage

1. **Run the Script:**
    - Save the script in a file, for example, `password_generator.py`.
    - Open a terminal or command prompt and run the script using a Python interpreter:
        
        ```bash
        python password_generator.py
        
        ```
        
2. **Customization:**
    - Modify the `length`, `include_digits`, and `include_special_chars` parameters when calling the `generate_password` function to customize the generated password.
3. **Generated Password:**
    - The script will generate and print a random password based on the specified criteria.

## Customization

- **Character Sets:**
    - Adjust the character sets in the `generate_password` function to include additional characters.
- **Password Logic:**
    - Customize the password generation logic based on specific requirements.

Feel free to use, modify, and share this script to generate strong and random passwords!

---

## Author

Jeel patel
