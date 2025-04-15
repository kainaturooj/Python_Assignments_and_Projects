# Function to get user data
def get_user_data():
    first_name :str = input("What is your first name?: ").strip()
    last_name :str = input("What is your last name?: ").strip()
    email :str = input("What is your email address?: ").strip()
    
    # Returning a tuple
    return first_name, last_name, email  

def main():
    # Call the function and store the returned tuple
    user_data :tuple = get_user_data()
    
    # Display the collected data
    print("Received the following user data:", user_data)
  


if __name__ == '__main__':
    main()