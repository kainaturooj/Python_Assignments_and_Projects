
# This program takes two integers from the user and prints the quotient and remainder of their division.
def main():
    
    # ask user to enter an number to be divided.
    dividend: int = int(input("\033[1;3mPlease enter an integer to be divided:\033[0m "))  
    
    # ask user to enter an number to divide by.
    divisor: int = int(input("\033[1;3mPlease enter an integer to divide by:\033[0m "))  

    # calculate the quotient and remainder of the division.
    quotient: int = dividend // divisor
    remainder: int = dividend % divisor

    # print the result of the division.
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == '__main__':
    main()