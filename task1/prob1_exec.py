# # Pre-populated user data dictionary for testing
# user_data = {}

# # Function to check if a password is valid
# def is_valid_password(password):
#     # Password rule: at least 8 characters, 1 uppercase, 1 lowercase, 1 digit, and 1 special character
#     if len(password) < 8:
#         return False
#     if not any(char.isupper() for char in password):
#         return False
#     if not any(char.islower() for char in password):
#         return False
#     if not any(char.isdigit() for char in password):
#         return False
#     if not any(char in "!@#$%^&*(),.?\":{}|<>" for char in password):
#         return False
#     return True

# # Function to check if age input is a valid integer
# def is_valid_age(age_input):
#     try:
#         age = int(age_input)
#         return age
#     except ValueError:  
#         return None

# # Function to check if a name only contains alphabetic characters
# def is_valid_name(name):
#     return name.isalpha()

# # Function to check if an email is valid without using regex
# def is_valid_email(email):
#     if "@" in email and "." in email:
#         local_part, domain = email.split("@", 1)
#         if "." in domain and local_part and domain:
#             return True
#     return False

# # Function for signing up a new user
# def signup():
#     while True:
#         email = input("Enter your email: ")
#         if is_valid_email(email):
#             if email in user_data:
#                 print("This email is already registered. Please sign in.")
#                 return
#             else:
#                 break
#         else:
#             print("Invalid email format. Please enter a valid email address.")

#     while True:
#         password = input("Enter your password: ")
#         if is_valid_password(password):
#             break
#         else:
#             print("Password does not meet the requirements.")
#             print("Password rule: At least 8 characters, 1 uppercase, 1 lowercase, 1 digit, and 1 special character.")
    
#     # Ensure first name is valid (alphabetical characters only)
#     while True:
#         first_name = input("Enter your first name: ")
#         if is_valid_name(first_name):
#             break
#         else:
#             print("First name should only contain alphabetic characters.")

#     # Ensure last name is valid (alphabetical characters only)
#     while True:
#         last_name = input("Enter your last name: ")
#         if is_valid_name(last_name):
#             break
#         else:
#             print("Last name should only contain alphabetic characters.")
    
#     # Ensure the age is an integer
#     while True:
#         age_input = input("Enter your age: ")
#         age = is_valid_age(age_input)
#         if age is not None:
#             break
#         else:
#             print("Please enter a valid integer for age.")

#     # Store user details in the user_data dictionary
#     user_data[email] = {
#         'password': password,
#         'first_name': first_name,
#         'last_name': last_name,
#         'age': age
#     }
    
#     print("Registration successful! You can now sign in.")

# # Function for signing in an existing user
# def signin():
#     email = input("Enter your email: ")
#     password = input("Enter your password: ")
    
#     # Check if user exists and password matches
#     if email in user_data and user_data[email]['password'] == password:
#         print(f"Welcome back, {user_data[email]['first_name']} {user_data[email]['last_name']}!")
#     else:
#         print("Invalid email or password. Please try again or sign up.")

# # Main menu function
# def main_menu():
#     while True:  
#         print("\n1. Signup\n2. Sign-in\n3. Exit")
#         choice = input("Choose an option: ")
        
#         if choice == '1':
#             signup()
#         elif choice == '2':
#             signin()
#         elif choice == '3':
#             print("Exiting the application. Goodbye!")
#             break
#         else:
#             print("Invalid option. Please choose again.")

# # Start the program
# main_menu()





# Class for handling user registration and login
class UserAuthentication:
    def __init__(self):
        self.user_data = {}

    # Function to check if a password is valid
    def is_valid_password(self, password)->bool:
        errors = []
        if len(password) < 8:
            errors.append("Password must be at least 8 characters long.")
        if not any(char.isupper() for char in password):
            errors.append("Password must contain at least 1 uppercase letter.")
        if not any(char.islower() for char in password):
            errors.append("Password must contain at least 1 lowercase letter.")
        if not any(char.isdigit() for char in password):
            errors.append("Password must contain at least 1 number.")
        if not any(char in "!@#$%^&*(),.?\":{}|<>" for char in password):
            errors.append("Password must contain at least 1 special character.")
        
        if errors:
            return False, errors
        return True, []

    # Function to check if age input is a valid integer and greater than 0
    def is_valid_age(self, age_input):
        try:
            age = int(age_input)
            if age > 0:
                return age
            else:
                print("Age must be greater than 0.")
                return None
        except ValueError:  
            return None

    # Function to check if a name only contains alphabetic characters
    def is_valid_name(self, name):
        return name.isalpha()

    # Function to check if an email is valid
    def is_valid_email(self, email):
        if "@" in email and "." in email:
            local_part, domain = email.split("@", 1)
            if "." in domain and local_part and domain:
                return True
        return False

    # Function for signing up a new user
    def signup(self):
        while True:
            email = input("Enter your email: ").lower()  # Convert email to lowercase
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
            valid, errors = self.is_valid_password(password)
            if valid:
                break
            else:
                for error in errors:
                    print(error)

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

        # Ensure the age is an integer greater than 0
        while True:
            age_input = input("Enter your age: ")
            age = self.is_valid_age(age_input)
            if age is not None:
                break
            else:
                print("Please enter a valid integer greater than 0 for age.")

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
        email = input("Enter your email: ").lower()  # Convert email to lowercase

        # Check if the user exists before asking for the password
        if email not in self.user_data:
            print("You need to sign up for an account before signing in.")
            return

        password = input("Enter your password: ")

        # Check if user exists and password matches
        if self.user_data[email]['password'] == password:
            print(f"Welcome back, {self.user_data[email]['first_name']} {self.user_data[email]['last_name']}!")
        else:
            print("Invalid password.")

    # Main menu function
    def main_menu(self):
        while True:  
            print("\n1. Signup\n2. Sign-in\n3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.signup()
            elif choice == '2':
                self.signin()
            elif choice == '3':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid option. Please choose again.")


# Start the program
if __name__ == "__main__":
    auth_system = UserAuthentication()
    auth_system.main_menu()
