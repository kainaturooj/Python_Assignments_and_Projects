def main():
    # Countdown from 10 to 1
    for i in range(10,0,-1):  # Starts from 10, goes to 1, decrementing by -1
        print(i, end=" ")  # Print numbers in the same line with space
    print("\033[1;3;34mLiftoff!\033[0m") # Print Liftoff! at the end


if __name__ == '__main__':
    main()