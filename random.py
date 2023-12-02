import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Please select at least one character type (letters, numbers, or symbols)!")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to Password Generator!")
    length = int(input("Enter the password length: "))
    use_letters = input("Include letters (yes/no): ").lower() == "yes"
    use_numbers = input("Include numbers (yes/no): ").lower() == "yes"
    use_symbols = input("Include symbols (yes/no): ").lower() == "yes"

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print("Generated password:", password)
    else:
        print("Password generation cancelled!")

if __name__ == "__main__":
    main()
