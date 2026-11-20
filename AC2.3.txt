users = {"user1": "password1", "user2": "password2"}

def is_valid_user(username):
    #Check if the username exists in the users dictionary
    return username in users

def check_password(username, password):
    #Check if the provided password matches the stored password for the username
    return users.get(username) == password

def login():
    #Prompt user for username and password and validate them
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    #check whether both fields have been completed before proceeding with authentication.
    if not username or not password:
        print("Please enter both your username and password.")
        return

    # Consolidating user existence and password validation into one check
    if is_valid_user(username) and check_password(username, password):
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Example usage
login()