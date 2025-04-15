# This program calculates the total number of seconds in a year.
# Useful constants to help make the math easier and cleaner!
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    # Calculate total seconds in a year using multiplication
    Seconds_in_Year: int = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    
    # Print the result in a nice formatted way
    print(f"There are {Seconds_in_Year} seconds in a year!")

# Call the main function
if __name__ == '__main__':
    main()