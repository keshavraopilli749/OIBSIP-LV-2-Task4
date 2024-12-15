import json
import hashlib

# File to store user data
USER_DATA_FILE = "users.json"

def load_users():
    """Load user data from the file."""
    try:
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    """Save user data to the file."""
    with open(USER_DATA_FILE, "w") as file:
        json.dump(users, file)

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password, confirm_password):
    """Register a new user."""
    users = load_users()

    if username in users:
        return "Username already exists. Please try a different one."

    if password != confirm_password:
        return "Passwords do not match. Please try again."

    users[username] = hash_password(password)
    save_users(users)
    return "Registration successful!"

def login(username, password):
    """Log in an existing user."""
    users = load_users()

    if username not in users:
        return False, "Username not found. Please register first."

    if users[username] != hash_password(password):
        return False, "Incorrect password. Please try again."

    return True, "Login successful!"

def secured_page():
    """Display a secured page for logged-in users."""
    return "Welcome! You have accessed the secured page."

def main():
    """Main function to run the authentication system."""
    predefined_inputs = [
        {"choice": "1", "username": "test_user", "password": "test_pass", "confirm_password": "test_pass"},
        {"choice": "2", "username": "test_user", "password": "test_pass"},
        {"choice": "3"}
    ]

    for input_set in predefined_inputs:
        choice = input_set.get("choice")

        if choice == "1":
            username = input_set.get("username")
            password = input_set.get("password")
            confirm_password = input_set.get("confirm_password")
            result = register(username, password, confirm_password)
            print(result)
        elif choice == "2":
            username = input_set.get("username")
            password = input_set.get("password")
            success, message = login(username, password)
            print(message)
            if success:
                print(secured_page())
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
