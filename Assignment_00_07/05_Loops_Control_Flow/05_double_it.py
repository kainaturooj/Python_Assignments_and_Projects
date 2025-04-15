def main():
    # Ask the user for a number and convert it to an integer
    curr_value :int = int(input("Enter a number: "))

    # Loop until curr_value is 100 or greater
    while curr_value < 100:

        # Double the value
        curr_value *= 2  
        print(curr_value, end=" ") 


if __name__ == '__main__':
    main()