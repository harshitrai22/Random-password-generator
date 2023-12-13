import random
import string


def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if length < 1:
        print("Password length must be at least 1.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Welcome to the Password Generator!")

    while True:
        length = int(input("Enter the length of the password: "))
        use_uppercase = input(
            "Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        generated_password = generate_password(
            length, use_uppercase, use_digits, use_symbols)

        if generated_password:
            print("\nGenerated Password:", generated_password)

        try_again = input("\nGenerate another password? (y/n): ").lower()
        if try_again != 'y':
            print("Exiting the Password Generator. Goodbye!")
            break


if __name__ == "__main__":
    main()
