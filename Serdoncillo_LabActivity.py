def display_menu():
    """Display a list of food items with their prices."""
    menu = {
        'Burger': 50,
        'Fries': 30,
        'Pizza': 100,
        'Soda': 20,
        'Ice Cream': 25
    }
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item}: PHP {price}")
    return menu

def get_order(menu):
    """Allow the user to choose an item from the menu."""
    while True:
        choice = input("\nEnter the food item you want to order: ").strip()
        if choice in menu:
            print(f"You selected: {choice}")
            return choice
        else:
            print("Invalid choice. Please select an item from the menu.")

def calculate_total(menu, item):
    """Calculate the total cost of the selected item."""
    return menu[item]

def process_payment(total):
    """Prompt the user to input cash and calculate the change."""
    while True:
        try:
            cash = float(input(f"\nYour total is PHP {total}. Enter cash amount: "))
            if cash >= total:
                change = cash - total
                print(f"Payment successful! Your change is PHP {change:.2f}.")
                break
            else:
                print(f"Insufficient amount. You need at least PHP {total - cash:.2f} more.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def main():
    """Main function to execute the food ordering system."""
    print("Welcome to the Food Ordering System!")
    menu = display_menu()
    item = get_order(menu)
    total = calculate_total(menu, item)
    process_payment(total)
    print("\nThank you for your order! Enjoy your meal.")

if __name__ == "__main__":
    main()