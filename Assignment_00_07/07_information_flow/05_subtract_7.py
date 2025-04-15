def subtract_seven(num :str):

    # Subtracts 7 from the given number
    return num - 7  

def main():

    # Get user input
    number :int = int(input("Enter a number: "))

     # Call the helper function  
    result :int = subtract_seven(number) 
    print("Result after subtracting 7:", result) 


if __name__ == '__main__':
    main()