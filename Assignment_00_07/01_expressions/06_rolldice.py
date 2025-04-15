# This program rolls two dice and prints the results and the total of the two dice.
import random

# to make the random number generator produce the same sequence of results.
# random.seed(99)

# number of sides on a die.
NUM_SIDES: int = 6

def main():

    # rolling the first die.
    die1: int = random.randint(1, NUM_SIDES)

    # rolling the second die.
    die2: int = random.randint(1, NUM_SIDES)
    
    # adding the two dice.
    total: int = die1 + die2

    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

if __name__ == '__main__':
    main()