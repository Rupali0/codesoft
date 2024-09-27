import random
import string  # Importing the string module

# Getting password length
length = int(input("Enter password length: "))

print('''Choose character set for password from these : 
        1. Letters
        2. Digits
        3. Special characters
        4. Exit''')

characterList = ""

# Getting character set for password
while(True):
    choice = int(input("Pick a number: "))
    if choice == 1:
        # Adding letters to possible characters
        characterList += string.ascii_letters
    elif choice == 2:
        # Adding digits to possible characters
        characterList += string.digits
    elif choice == 3:
        # Adding special characters to possible characters
        characterList += string.punctuation
    elif choice == 4:
        break
    else:
        print("Please pick a valid option!")

if characterList:
    password = []

    # Generating the password
    for i in range(length):
        randomchar = random.choice(characterList)
        password.append(randomchar)

    # Printing password as a string
    print("The random password is: " + "".join(password))
else:
    print("No character sets selected, cannot generate a password.")
