import getpass

#using lowercase keys to support case-insensitive lookups
users = {"user1": "password1", "user2": "password2", "audreym": "password3"}

def login():
    attempts = 3
    for attempt in range(1, attempts + 1):
	#convert username input to lowercase tand strip whitespaces immediately
        username = input("Enter your username: ").strip().lower()
        password = getpass.getpass("Enter your password: ").strip()

        if not username or not password:
            print("Please enter both your username and password.\n")
            continue

        # Securely authenticate using dictionary lookup in a single step
        if users.get(username) == password:
            print("Login successful!")
            return
        
        remaining = attempts - attempt
        if remaining > 0:
            print(f"Invalid username or password. You have {remaining} attempt(s) left.\n")
        else:
            print("Sorry! Access denied: Too many incorrect attempts. Login session locked.")

# Example usage
login()