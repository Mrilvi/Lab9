'''

This is Maria Ilieva's main and encode functions file
Working with Allan Rivera - Jaramillo

'''

# encode password function by Maria Ilieva
def encode(password):
    pass_encoded = ""
    for num in password:
        shifted_num = str((int(num) + 3) % 10)
        pass_encoded += shifted_num
    return pass_encoded

# decode password function to be written by Allan Rivera - Jaramillo
def decode(password):
    pass

# main program by Maria Ilieva
if __name__ == '__main__':
    while True:

        # create menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")

        # var for user input
        menu_choice = input("Please enter an option: ")

        # encode the given password
        if menu_choice == "1":
            # var for the user inputted password
            pass_to_encode = input("Please enter your password to encode: ")
            # var for the encoded password
            encoded_pass = encode(pass_to_encode)
            print("Your password has been encoded and stored!")
            print("")

        # show encoded passord and original password using the decode function, created by partner
        elif menu_choice == "2":
            print(f"The encoded password is: {encoded_pass}, and the original password is {decode(encoded_pass)}.")
            print("")

        # quit program
        elif menu_choice == "3":
            break


