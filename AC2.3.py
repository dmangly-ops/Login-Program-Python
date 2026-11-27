import getpass

# Using lowercase keys to support case-insensitive lookups
users = {"user1": "password1", "user2": "password2", "audreym": "password3", "manglya": "password4"}

def login():
    attempts = 3
    for attempt in range(1, attempts + 1):
        # Convert username input to lowercase and strip whitespaces immediately
        username = input("Enter your username: ").strip().lower()

        if not username:
            print("Please enter a username.\n")
            continue

        # If username doesn't exist, offer to register it
        if username not in users:
            register = input(f"Username '{username}' not found. Would you like to register? (yes/no): ").strip().lower()
            if register == 'yes':
                # Explicit prevention check
                if username in users:
                    print("Registration failed: This username is already registered.\n")
                    continue

                # Adding a hint to explain password masking to user
                print("[Hint: Characters will not be visible on screen while typing for security]")
                new_password = getpass.getpass("Create a password for your new account: ").strip()
                if len(new_password) < 7:
                    print("Sorry! Your registration has failed. Password must be at least 7 characters long for security.\n")
                elif new_password:
                    users[username] = new_password
                    print(f"Congratulations! You have successfully registered and logged in as '{username}'!\n")
                    return  # Automatically log in the user upon successful registration and exit
                else:
                    print("Password field cannot be empty. Your registration is cancelled.\n")
            continue

        # Hint for secure password entry during login
        print("[Hint: Characters will not be visible on screen while typing for security]")
        password = getpass.getpass("Enter your password: ").strip()

        if not password:
            print("Please enter your password.\n")
            continue

        # Securely authenticate using dictionary lookup in a single step
        if users.get(username) == password:
            print(f"Login successful! Welcome, {username}!\n")
            return

        remaining = attempts - attempt
        if remaining > 0:
            print(f"Invalid username or password. You have {remaining} attempt(s) left.\n")
        else:
            print("Sorry! Access denied: Too many incorrect attempts. Login session locked.")

# Example usage
login()
