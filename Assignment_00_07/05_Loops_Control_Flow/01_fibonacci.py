
# "Start with 0 and 1, and keep adding the last two numbers 
# to make the next one. Keep printing these numbers until the value reaches 10,000."
def main():

    # Constant value , limit to print the sequence .
    MAX_VALUE = 10000  

    # Starting values of Fibonacci sequence
    # a, b = 0, 1
    
    #another way  
    a = 0  
    b = 1
    # Print Fibonacci numbers until we reach MAX_VALUE
    while a < MAX_VALUE:

        # print sequence in a one line with spaces.
        print(a, end=" ")

        # this way of writing this is called unpacking the tuple 
        # upadte the value of variable at once time. 
        a, b = b, a + b  
        

# Required to call the main function
if __name__ == '__main__':
    main()