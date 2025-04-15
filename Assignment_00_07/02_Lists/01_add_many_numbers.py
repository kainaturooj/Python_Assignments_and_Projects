# This program adds a list of numbers and returns the sum
def sum_of_numbers(numbers) -> int:
    # total = 0
    for num in numbers:
        total += num
        
    return total

def main():
    # Get the number of numbers to add
    numbers_list :list[int] = [10, 20, 30, 40, 50]

    # Call the sum_of_numbers function passing with the list of numbers
    result :int = sum_of_numbers(numbers_list)

    # Print the list and the sum of the numbers
    print("List:", numbers_list)
    print("Sum of numbers:", result)

if __name__ == '__main__':
    main()