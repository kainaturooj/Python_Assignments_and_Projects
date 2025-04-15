def greet(name):
   
    print(f"Salam {name}!")

def main():
    # Ask the user for their name
    name :str = input("What's your name? ")
    
    # Call the greet function with the user's name
    greet(name)

# Required line to run the program
if __name__ == '__main__':
    main()