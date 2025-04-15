# this program will double the element of iist.
def main():

    numbers :int = [1, 2, 3, 4]
    

    for i in range(len(numbers)):
        numbers[i] *= 2  


    print("Doubled List:", numbers)


if __name__ == '__main__':
    main()