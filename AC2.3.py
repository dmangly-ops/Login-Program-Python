users = {"user1": "password1", "user2": "password2"}


def is_valid_user(username):
    #Check if the username exists in the users dictionary
    return username in users

def check_password(username, password):
    #Check if the provided password matches the stored password for the username
    return users.get(username) == password

def login():
    attempts = 3
    for attempt in range(1, attempts + 1):
        #Prompt user for username and password and validate them
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        #check whether both fields have been completed before proceeding with authentication.
        if not username or not password:
            print("Please enter both your username and password.\n")
            continue

        # Consolidating user existence and password validation into one check
        if is_valid_user(username) and check_password(username, password):
            print("Login successful!")
            return
        else:
            remaining = attempts - attempt
            if remaining > 0:
                print(f"Invalid username or password. You have {remaining} attempt(s) left.\n")
            else:
                print("Too many incorrect attempts. Login session locked.")

# Example usage
login()