# conversion factor from feet to inches.
INCHES_IN_FOOT = 12  # 1 foot = 12 inches

def main():
    
    # ask user to enter the number of feet to convert into inches.
    feet : float = float(input("\033[1;3m Enter number of feet: \033[0m"))  
    
    # calculate the number of inches.
    inches : float = feet * INCHES_IN_FOOT  
    
    # print the result.
    print(f"That is {inches} inches!")

if __name__ == '__main__':
    main()