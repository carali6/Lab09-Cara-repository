# This is Xinye (Cara) Li's main function and encoder part.

def menu():
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")

def encode():
    password = input("Please enter your password to encode: ")
    result = ""
    for letter in password:
        if letter == "0":
            result += "3"
        elif letter == "1":
            result += "4"
        elif letter == "2":
            result += "5"
        elif letter == "3":
            result += "6"
        elif letter == "4":
            result += "7"
        elif letter == "5":
            result += "8"
        elif letter == "6":
            result += "9"
        elif letter == "7":
            result += "0"
        elif letter == "8":
            result += "1"
        elif letter == "9":
            result += "2"
    print("Your password has been encoded and stored!")
    return result

def main():
    menu()
    option = input("Please enter an option: ")
    if option == "1":
        encode()

if __name__ == "__main__":
    main()