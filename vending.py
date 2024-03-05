# Vending machine items and prices
items = {
    '1': {'name': 'Candy', 'price': 1.25},
    '2': {'name': 'Chips', 'price': 1.50},
    '3': {'name': 'Soda', 'price': 2.00},
    '4': {'name': 'Water', 'price': 1.00}
}

# Display available items and prices
print("Welcome to the Vending Machine!")
print("Please select an item:")

for key, item in items.items():
    print(f"{key}. {item['name']} - ${item['price']}")

# Prompt user for input
selection = input("Enter the item number you wish to purchase: ")

# Check if the selected item is valid
if selection in items:
    selected_item = items[selection]
    print(f"You have selected {selected_item['name']}.")
    amount_due = selected_item['price']

    # Prompt user to insert money
    while amount_due > 0:
        try:
            payment = float(input(f"Please insert ${amount_due:.2f}: "))
            if payment >= amount_due:
                change = payment - amount_due
                print(f"Thank you for your purchase! Your change is ${change:.2f}.")
                break
            else:
                print("Insufficient payment. Please insert more money.")
                amount_due -= payment
        except ValueError:
            print("Invalid payment amount. Please enter a valid number.")
else:
    print("Invalid selection. Please try again.")
