balance = 1000

while True:
    print("--------------------------------------")
    print("|   Simple Money Withdrawal System   |")
    print("--------------------------------------")
    print("Menu:")
    print("1. Withdraw")
    print("2. Check Balance")
    print("3. Exit")

    choices = input("Go to: ")

    if choices == "1":
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Invalid amount.")

            elif amount > balance:
                print("Insufficient funds.")

                while True:
                    print("\nOptions:")
                    print("1. Exit")
                    print("2. Check Balance")
                    print("3. Re-enter amount")

                    options = input("Go to: ")

                    if options == "1":
                        print("Program ended.")
                        exit()

                    elif options == "2":
                        print("Current balance:", balance)

                    elif options == "3":
                        try:
                            newAmount = float(input("Enter new amount: "))

                            if newAmount <= 0:
                                print("Invalid amount.")

                            elif newAmount > balance:
                                print("Insufficient funds.")

                            else:
                                balance = balance - newAmount
                                print("Successfully withdrawn.")
                                break
                        except ValueError:
                            print("Invalid input.")

                    else:
                        print("Invalid choice.")
            else:
                balance = balance - amount
                print("Successfully withdrawn.")

        except ValueError:
            print("Invalid input.")

    elif choices == "2":
        print("Current balance:", balance)

    elif choices == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")