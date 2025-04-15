# this program create the list according to user's prompt and ill print the first element from the list.

# function print the first element.
def get_first_element(lst) -> str:
    """ Prints the first element of a given non-empty list. """
    print("The first element in the list is:", lst[0])

# take input from user's for numbers of elements in want to add in empty list.
def main():

    user_num_of_element :int = int(input("Enter the number of elements in the list: "))
    lst = []

    for i in range(user_num_of_element):
        element :str = input(f"Enter element {i+1}: ")
        lst.append(element)  


    get_first_element(lst)

# Required line to run the program
if __name__ == '__main__':
    main()