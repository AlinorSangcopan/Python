class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self):
        item = input("Enter item to add: ")
        self.cart.append(item)
        
        print("Added successfully.")

    def remove_item(self):
        print(self.cart)
        item = int(input("Enter index to remove: "))
        self.cart.pop(item)
            
        print("Removed successfully.")

    def view_cart(self):
        if len(self.cart) == 0:
            print("Your cart is empty.")
        else:
            print("\nItems in your cart:")
            print(self.cart)

    def checkout(self):
        if len(self.cart) == 0:
            print("Your cart is empty.")
        else:
            print("\nChecking out the following items:")
            print(self.cart)
            print("Checkout successful.")
            self.cart.clear()

cart = ShoppingCart()

while True:
    print("\nShopping Cart Menu")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        cart.add_item()

    elif choice == "2":
        cart.remove_item()

    elif choice == "3":
        cart.view_cart()

    elif choice == "4":
        cart.checkout()
        break

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")