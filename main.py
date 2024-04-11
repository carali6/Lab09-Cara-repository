print("Hi Cara")

def display_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode():
    password = input("Please enter your password to encode:")
    new_password = ""
    for letter in password:

        if letter == "0":
            new_password += "3"
        elif letter == "1":
            new_password += "4"
        elif letter == "2":
            new_password += "5"
        elif letter == "3":
            new_password += "6"
        elif letter == "4":
            new_password += "7"
        elif letter == "5":
            new_password += "8"
        elif letter == "6":
            new_password += "9"
        elif letter == "7":
            new_password += "0"
        elif letter == "8":
            new_password += "1"
        elif letter == "9":
            new_password += "2"


def main():
    while True:
        option = int(input("Please enter an option:"))

        if option == 1:
            encode()
            print("Your password has been encoded and stored!")


