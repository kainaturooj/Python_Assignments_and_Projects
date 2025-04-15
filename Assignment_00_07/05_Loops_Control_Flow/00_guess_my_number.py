import random

def main():
    # Random number generating between 0 and 99
    secret_number :int = random.randint(1, 99)  
    print("I am thinking of a number between 1 and 99...")

    while True:
        try:

            # User input for guessing number.
            guess_number :int = int(input("Enter a guess: ")) 
 
            if guess_number < secret_number:
                print("Your guess is too low")
            elif guess_number > secret_number:
                print("Your guess is too high")
            else:
                print(f"Congrats! The number was: {secret_number}")

                # Exit loop when correct the user's guess number.
                break

         # Handle non-integer inputs     
        except ValueError:
            print("Please enter a valid number!") 

if __name__ == '__main__':
    main()