from auth_sys import UserManagement


def menu():
    print("Menu:")
    print("1. Signup")
    print("2. Sign-in")
    print("3. Exit")

def main():
    user_management = UserManagement()

    while True:
        menu()    
        choice  = input("choose an option 1,2 or 3:")
        if (choice == "1"):
            user_management.signup()
        elif (choice == "2"):
            user_management.signin() 
        elif (choice == "3"):
            print("Exiting the application. Goodbye!")
            return
        else:
            print("Incorrect input, try again") 


if __name__ == "__main__":
    main()
