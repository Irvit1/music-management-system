"""
Create a singleton for Song Management System as in single

Create a menu driven function which will be used to run the function

"""

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from song_management_sys import SongsManagementSystem
from custom_exceptions import EmptyDatabaseException

def menu():
    print("\nDeveloper Menu:")
    print("1. Load Song Data")
    print("2. View Songs Database")
    print("3. Delete a Song")
    print("4. Modify a Song")
    print("5. Exit")

def main():
    management_system = SongsManagementSystem()

    while True:
        menu()
        choice = input("Select an option: ")
        print("\n")
        if choice == "1":
            file_name = input("Enter the file name: ")
            management_system.load_song_data(file_name)
        elif choice == "2":
            management_system.view_song_database()
        elif choice == "3":
            try:
                if management_system.is_database_empty():
                    raise EmptyDatabaseException()
                artist = management_system.get_valid_artist()
                title = input("Enter the song title: ")
                management_system.delete_song(artist, title)
            except EmptyDatabaseException as e:
                print(e)
        elif choice == "4":
            try:
                if management_system.is_database_empty():
                    raise EmptyDatabaseException()
                artist = management_system.get_valid_artist()
                title = input("Enter the song title: ")
                management_system.modify_song(artist, title)
            except EmptyDatabaseException as e:
                print(e)
        elif choice == "5":
            print("Thank you for using the Song Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
