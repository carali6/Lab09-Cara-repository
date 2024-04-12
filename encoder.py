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

def decode(encoded_password):
    result = ""
    for letter in encoded_password:
        if letter == "3":
            result += "0"
        elif letter == "4":
            result += "1"
        elif letter == "5":
            result += "2"
        elif letter == "6":
            result += "3"
        elif letter == "7":
            result += "4"
        elif letter == "8":
            result += "5"
        elif letter == "9":
            result += "6"
        elif letter == "0":
            result += "7"
        elif letter == "1":
            result += "8"
        elif letter == "2":
            result += "9"
    return result


def main():
    menu()
    while True:
        option = input("Please enter an option: ")
        if option == "1":
            encoded_password = encode()
        elif option == "2":
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password},and the original password is:", decoded_password)
        elif option == "3":
            break
        else:
            print("Please enter a valid option 1 - 3")

if __name__ == "__main__":
    main()