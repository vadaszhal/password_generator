# required modules
import string
import random

# possible characters
characters = list(string.ascii_letters + string.digits + "&#@!+")

# function with while loop and error handling
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

# generate password with for loop
    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = ''.join(password)
    print(password)
# main function to handle user input
def main():
    while True:
        option = input("Do you want to generate a password? (y/n): ").strip().lower()

        if option == 'y':
            generate_password()
            break
        elif option == 'n':
            print("Password generation cancelled.")
            break
        else:
            print("Invalid option. Please enter 'y' or 'n'.")
    
if __name__ == "__main__":
    main()