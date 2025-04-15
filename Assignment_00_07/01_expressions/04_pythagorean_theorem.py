import math  

def main():
    
    # ask user to enter the length of AB of right angle triangle.
    ab : float = float(input("\033[1m\033[3mEnter the length of AB:\033[0m "))  
    
    # ask user to enter the length of AC of right angle triangle.
    ac : float = float(input("\033[1m\033[3mEnter the length of AC:\033[0m "))  

    # calculate the length of BC using the Pythagorean theorem.
    bc = math.sqrt(ab**2 + ac**2)  

    # print the length of BC (the hypotenuse) is.
    print(f"The length of BC (the hypotenuse) is: {bc}")  

if __name__ == '__main__':
    main()