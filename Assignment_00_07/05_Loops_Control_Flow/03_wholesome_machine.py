def main():
    affirmation = "I am capable of doing anything, I put my mind to."
    print(f"Please type the following affirmation: {affirmation}")

    while True:

         # This makes user input appear in blue
        user_input :str = input("\033[34m")

        # Resets color back to normal 
        print("\033[0m", end="")  

        if user_input == affirmation:
            print("That's right! :)")
            break
        else:
            print("Hmmm That was not the affirmation. Please type the following affirmation:", affirmation)



if __name__ == '__main__':
    main()