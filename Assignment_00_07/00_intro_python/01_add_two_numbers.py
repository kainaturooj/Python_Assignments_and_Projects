def main():
    
    # take input number from user 
    num1 :str = input("\033[1;3m Enter the first number: \033[0m")
    
    
    # convert string to integer
    num1 :int = int(num1)

    
    
    # take another input number from user 
    num2 :str = input("\033[1;3m Enter the second number: \033[0m")
    
    # convert string to integer
    num2 :int = int(num2)
    
    
    # calculate the total sum
    total_sum :int = num1 + num2
    
    print(f"\033[1;3m The total sum is: {total_sum} \033[0m")

if __name__ == "__main__":
    main()