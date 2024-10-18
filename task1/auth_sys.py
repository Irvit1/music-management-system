from user import User


class UserManagement:
    
    def __init__(self):
        # Pre-populated user data dictionary for testing
        self.user_data = {}

    # Function to check if a password is valid
    def is_valid_password(self, password):
        # Password rule: at least 8 characters, 1 uppercase, 1 lowercase, 1 digit, and 1 special character
        if len(password) < 8:
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char in "!@#$%^&*(),.?\":{}|<>" for char in password):
            return False
        return True

    # Function to check if age input is a valid integer
    def is_valid_age(self, age_input):
        try:
            age = int(age_input)
            if age < 0:
                print("Age cannot be negative.")  # Print statement for negative age
                return None
            return age
        except ValueError:
            print("Invalid input. Please enter a valid number.")  # Print statement for invalid input
            return None

    # Function to check if a name only contains alphabetic characters
    def is_valid_name(self, name):
        return name.isalpha()

    # Function to check if an email is valid without using regex
    def is_valid_email(self, email):
        if "@" in email and "." in email:
            local_part, domain = email.split("@", 1)
            if "." in domain and local_part and domain:
                return True
        return False

    # Function for signing up a new user
    def signup(self):
        while True:
            email = input("Enter your email: ").lower().strip()
            if self.is_valid_email(email):
                if email in self.user_data:
                    print("This email is already registered. Please sign in.")
                    return
                else:
                    break
            else:
                print("Invalid email format. Please enter a valid email address.")

        while True:
            password = input("Enter your password: ")
            if self.is_valid_password(password):
                break
            else:
                print("Password does not meet the requirements.")
                print("Password rule: At least 8 characters, 1 uppercase, 1 lowercase, 1 digit, and 1 special character.")
        
        # Ensure first name is valid (alphabetical characters only)
        while True:
            first_name = input("Enter your first name: ")
            if self.is_valid_name(first_name):
                break
            else:
                print("First name should only contain alphabetic characters.")

        # Ensure last name is valid (alphabetical characters only)
        while True:
            last_name = input("Enter your last name: ")
            if self.is_valid_name(last_name):
                break
            else:
                print("Last name should only contain alphabetic characters.")
        
        # Ensure the age is an integer
        while True:
            age_input = input("Enter your age: ")
            age = self.is_valid_age(age_input)
            if age is not None:
                break
            else:
                continue

        # Store user details in the user_data dictionary
        self.user_data[email] = {
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'age': age
        }
        
        print("Registration successful! You can now sign in.")


    # Function for signing in an existing user
    def signin(self):
        email = input("Enter your email: ").lower().strip()
        password = input("Enter your password: ")
        
        # Check if user exists and password matches
        if email in self.user_data:
           if self.user_data[email]['password'] == password:
             print(f"Welcome back, {self.user_data[email]['first_name']} {self.user_data[email]['last_name']}!")
           else:
             print("Incorrect password or email address")  
        else:
            print("Invalid email, please sign up")


# Start the program
if __name__ == "__main__":
    user_management = UserManagement()
    user_management.main_menu()
