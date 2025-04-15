# this program will tell the height of users for allowing to ride.
def main():
    while True:
        # taking input for height from users
        height :str = input("\033[1;3mHow tall are you?\033[0m")

        # if users press enter without write  height program will stop.
        if height == "":
            print("\033[1;3mGoodBye program is over, Have a great day!\033[0m")
            break

        # converting height into integer.
        height :int = int(height)

        # checking the height.
        if height >= 50:
            print("You're tall enough to ride!\n")
        else:
            print("You're not tall enough to ride, but maybe next year!\n")


if __name__ == '__main__':
    main()