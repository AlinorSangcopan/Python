try:
    file = open("message.txt", "x")
    print("File created successfully!")
    file.close()

except FileExistsError:
    print("File already exists!")

while True:
    print("\nWelcome to Messaging App")
    print("1. Send Message")
    print("2. View Messages")
    print("3. Exit")

    choices = input("Enter Choice: ")

    if choices == "1":
        with open("message.txt", "a") as file:
            file.write(input("Enter your message: ") + "\n")
            print("Message sent!")

    elif choices == "2":
        with open("message.txt", "r") as file:
            print(file.read())

    elif choices == "3":
        break

    else:
        print("Invalid choices.")