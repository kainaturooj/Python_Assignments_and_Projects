# this program will print the user's age and and also tell him they are eligible for voting in respective country or not.
def main():
    # taking user's age.
    age :int = int(input("How old are you? "))

    # checking the age for voting eligibiity.
    if age >= 16:
        print("You can vote in Peturksbouipo where the voting age is 16.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16.")

    if age >= 25:
        print("You can vote in Stanlau where the voting age is 25.")
    else:
        print("You cannot vote in Stanlau where the voting age is 25.")

    if age >= 48:
        print("You can vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Mayengua where the voting age is 48.")

# Yeh line program ko run karne ke liye zaroori hai
if __name__ == '__main__':
    main()




