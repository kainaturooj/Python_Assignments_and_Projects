def main():
    # Dictionary storing fruit prices (per unit)
    fruit_prices = {
        "apple": 3.5,
        "durian": 15.0,
        "jackfruit": 20.0,
        "kiwi": 2.5,
        "rambutan": 5.0,
        "mango": 7.0
    }
    
    # Initialize total cost
    total_cost = 0  

    # Loop through each fruit in the dictionary
    for fruit, price in fruit_prices.items():
        quantity = int(input(f"How many ({fruit}) do you want?: "))  # User input
        total_cost += quantity * price  # Multiply quantity with price

    # Print total cost
    # Display in 2 decimal places
    print(f"\nYour total is ${total_cost:.2f}")  


if __name__ == '__main__':
    main()