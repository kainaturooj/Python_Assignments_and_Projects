# Function to check the stock of a given fruit
def num_in_stock(fruit):
    inventory = {
        "apple": 500,
        "banana": 300,
        "pear": 1000,
        "orange": 250,
        "mango": 700
    }

    # Return stock count or 0 if not found
    return inventory.get(fruit.lower(), 0)  

def main():
    # Prompt the user for input
    fruit :str = input("Enter a fruit: ").strip()

    # Get the number of fruit in stock
    stock :int = num_in_stock(fruit)

    # Print appropriate message based on stock availability
    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")


if __name__ == '__main__':
    main()