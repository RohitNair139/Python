print("Welcome to Pizza Delivery!")


size = input("Enter the size of the pizza (S, M, or L): ").upper()
pepperoni = input("Do you want pepperoni? (Y/N): ").upper()
cheese = input("Do you want extra cheese? (Y/N): ").upper()


base_prices = {
    "S": 15,
    "M": 20,
    "L": 25
}

pepperoni_prices = {
    "S": 2,
    "M": 3,
    "L": 3
}

cheese_price = 1


if size not in base_prices:
    print("Invalid pizza size selected.")
else:
    # Start with base price
    final_bill = base_prices[size]

    # Add pepperoni if selected
    if pepperoni == "Y":
        final_bill += pepperoni_prices[size]

    # Add cheese if selected
    if cheese == "Y":
        final_bill += cheese_price


    print("\n--- Order Summary ---")
    print(f"Pizza Size      : {size}")
    print(f"Pepperoni Added : {'Yes' if pepperoni == 'Y' else 'No'}")
    print(f"Extra Cheese    : {'Yes' if cheese == 'Y' else 'No'}")
    print(f"Total Bill      : ${final_bill}")
