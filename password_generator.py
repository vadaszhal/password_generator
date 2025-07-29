import string
import random

characters = list(string.ascii_letters + string.digits + "&#@!+")
def generate_password():
    while True:
        try:
            password_length = int(input("Enter the desired password length (8–12): "))
        except ValueError:
            print("Invalid input: please enter a number.")
            continue

        if 8 <= password_length <= 12:
            break
        else:
            print("Password length must be between 8 and 12 characters. Please try again.")
    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = ''.join(password)
    print(password)

option = input("Do you want to generate a password? (y/n): ").strip().lower()

if option == 'y':
    generate_password()
    quit()
elif option == 'n':
    print("Password generation cancelled.")
    quit()
else:
    print("Invalid option. Please enter 'y' or 'n'.")
    quit()