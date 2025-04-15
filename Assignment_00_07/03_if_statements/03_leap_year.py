# this program will check user's inputed year is leap or not leap year.
def main():
    # Get the year to check from the user
    year :int = int(input('Please input a year: '))
    
    # Checking whether the provided year is evenly divisibly by 4
    if year % 4 == 0:

         # Checking whether the provided year is evenly divisibly by 100  
        if year % 100 == 0: 

             # Checking whether the provided year is evenly divisibly by 400
            if year % 400 == 0: 
                print("That's a leap year!")

            # (Not divisible by 400)    
            else:  
                print("That's not a leap year.")
        
        # (Not divisible by 100)
        else:  
            print("That's a leap year!")
    
    # (Not divisible by 4)
    else:  
        print("That's not a leap year.")




if __name__ == '__main__':
    main()


