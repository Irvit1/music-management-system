"""
Create a singleton for Song Management System User as in single instance

Create a menu driven function which will be used to run the function

"""
from song_management_sys_user import SongsManagementSystemUser

def menu():
    print("1. Search for song by title:")
    print("2. Search for all songs by artist")
    print("3. Exit")

def main():
    management_user =  SongsManagementSystemUser()
    management_user.load_song_data()
    menu()

    while True:
        
        choice = input("Select an option : ")
        if choice == "1":
            management_user.search_song()

        elif choice == "2":
            management_user.same_artist_songs()
            
        elif choice == "3":
            print("Goodbye")
            break

        else:
            print("Invadid choice, try again")            

if __name__ == "__main__":
    main()       