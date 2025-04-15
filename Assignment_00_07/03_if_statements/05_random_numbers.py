# this programe will generate the 10 random number between 1 to 100.
import random  

def main():
    # generating 10 random numbers in form of list
    random_numbers = [random.randint(1, 100) for _ in range(10)]

    # unpack the list with asteric symbol and also separated with space.
    print(*random_numbers)
    

    # another way to doing.
    # for _ in range(10):
    #     num = random.randint(1, 100)
    #     print(num , end=" ")
     


if __name__ == '__main__':
    main()