
# function to double the number.
def double(num :int):
    return num * 2

def main():
    num :int = int(input("\033[94mEnter a number: \033[0m"))
    result = double(num)
    print(f"Double that is {result}")

if __name__ == '__main__':
    main()