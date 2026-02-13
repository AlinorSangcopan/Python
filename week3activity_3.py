while True:
    password = input("Enter password: ")

    hasLetter = any(char.isalpha()for char in password)
    hasNum = any(char.isdigit()for char in password)

    if hasLetter and hasNum:
        print("Password accepted.")
        break
    else:
        print("Invalid password. Try again.")