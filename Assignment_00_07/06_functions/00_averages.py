def find_average(num1:float, num2:float)-> float:

    # add the two numbers and dvided by 2 that is average.
    return (num1 + num2) / 2

def main():
    # Taking input for number in decimal from the user
    num1:float = float(input("Enter the first number: "))
    num2:float = float(input("Enter the second number: "))
    
    # Calculating and displaying the average
    average:float = find_average(num1, num2)
    print(f"The average of {num1} and {num2} is: {average}")

if __name__ == '__main__':
    main()