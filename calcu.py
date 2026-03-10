num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

while True:
    print("\nSelect choices: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choices = input("Enter your choice: ")

    if choices == "1":
        answer = num1 + num2
        print("Result:", answer)

    elif choices == "2":
        answer = num1 - num2
        print("Result:", answer)

    elif choices == "3":
        answer = num1 * num2
        print("Result:", answer)

    elif choices == "4":
        if num2 != 0:
            answer = num1 / num2
            print("Result:", answer)
        else:
            print("Undefined.")

    elif choices == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")