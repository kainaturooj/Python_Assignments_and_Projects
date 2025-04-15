def in_range(n, low, high):
    
    return low <= n <= high

def main():
    # Ask the user for input
    n :int = int(input("Enter a number: "))
    low :int = int(input("Enter the lower limit: "))
    high :int = int(input("Enter the upper limit: "))

    # Call the in_range function and print the result
    result :int = in_range(n, low, high)
    print(result)


if __name__ == '__main__':
    main()