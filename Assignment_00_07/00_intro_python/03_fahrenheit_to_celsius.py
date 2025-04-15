def main():
    # take input for temperature in fahrenheit from user
    fahrenheit :float = float(input("\033[1;3m Enter temperature in Fahrenheit: \033[0m"))

    
    # convert fahrenheit to celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    print(f"Temperature: {fahrenheit}F = {celsius}C")



if __name__ == '__main__':
    main()