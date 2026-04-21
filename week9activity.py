contacts = []

while True:
    print("\nContact Manager")
    print("1. View contacts")
    print("2. Add a contact")
    print("3. Remove a contact")
    print("4. Exit")

    option = input("Enter choice: ")

    if option == "1":
        print("Contacts:", contacts)

    elif option == "2":
        addName = input("Enter contact to add: ")
        contacts.append(addName)
        print("Added successfully")

    elif option == "3":
        removeName = input("Enter contact to remove: ")
        if removeName in contacts:
            contacts.remove(removeName)
            print("Removed successfully")

        else:
            print("Contact not found!")

    elif option == "4":
        print("Exiting program....")
        break

    else:
        print("Invalid choice!")