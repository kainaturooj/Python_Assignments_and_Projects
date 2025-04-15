
ADULT_AGE :int = 18  

def is_adult(age):
    
    return age >= ADULT_AGE  

def main():
    # Ask the user for their age
    age :int = int(input("How old is this person?: "))
    
    
    print(is_adult(age))


if __name__ == '__main__':
    main()