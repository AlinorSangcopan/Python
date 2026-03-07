users = []

while True:
    print("\nMenu")
    print("1. Show users")
    print("2. Add user")
    print("3. Update user")
    print("4. Delete user")
    print("5. Exit")

    choices = input("Enter your choice: ")

    if choices == "1":
        print(users)

    elif choices == "2":
        name = input("Enter name to add: ")
        users.append(name)

        print("\nAdded successfully.")

    elif choices == "3":
        update = int(input("Enter index to update: "))
        newName = input("Enter new name: ")
        users[update] = newName

        print("\nChanged successfully.")

    elif choices == "4":
        remove = int(input("Enter index to delete: "))
        users.pop(remove)

        print("\nDeleted successfully.")

    elif choices == "5":
        print("\nProgram ended.")
        break

    else:
        print("\nInvalid choice.")