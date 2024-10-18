"""
Create a singleton for Song Management System User as in single instance

Create a menu driven function which will be used to run the function

"""

import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from song_management_sys_user import SongManagementSystemUser


def menu():
    print("\n--- User Menu ---")
    print("1. Search for a Song by Title")
    print("2. Search for All Songs by an Artist")
    print("3. Exit")

def main():
    filename = "songs.txt"
    user = SongManagementSystemUser(filename)

    # Now just implement a while loop to run the menu and call the respective functions
    # choice 1 -> ask for title and call search_song_by_title
    # choice 2 -> ask for artist and call search_songs_by_artist
    # choice 3 -> exit the program
    # Also, check if the choice is invalid and print a message to the user

    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter the title of the song: ")
            user.search_song_by_title(title)
        elif choice == "2":
            artist = input("Enter the name of the artist: ")
            user.search_songs_by_artist(artist)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
