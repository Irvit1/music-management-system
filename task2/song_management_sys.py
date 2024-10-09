"""
Create a class named SongsManagementSystem
    fetch the songs data in init method

    Create function load_song_data
    filename, filepath as input variables
    -> Implement file handling and error handling in this function to fetch the data and store it in dictionary
    {
    "artist_name": [
        {
            "Title": "I Will Always Love You",
            "Album": "The Bodyguard",
            "Genre": "Soundtrack",
            "Duration": "4:31"
        },
        {
            "Title": "I Will Always Love You",
            "Album": "The Bodyguard",
            "Genre": "Soundtrack",
            "Duration": "4:31"
        },

    ]
    }

    Create a function to view database

    Create a function to delete song
        Artist name and title as arguments

    Create a function to modify database
        Artist name and title as arguments
"""
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import delete_file_entry, read_file, update_file_entry, write_file
from custom_exceptions import ArtistNotFoundException, EmptyDatabaseException, InvalidFileFormatError, SongNotFoundException
from song import Song

class SongsManagementSystem:

    def __init__(self) -> None:
        self.database = {}
        self.file_path = "../music-management-system/database"
        self.database_file = None

    def load_song_data(self, file_name: str) -> None:
        self.database_file = file_name
        unique_songs = set()
        try:
            song_data = read_file(self.file_path, file_name)
            for line in song_data:
                data = line.strip().split(',')
                if len(data) == 5:
                    title, artist, album, genre, duration = data
                    song = Song(title, artist, album, genre, duration)

                    if song not in unique_songs:
                        unique_songs.add(song)
                        self._add_song(song)
                else:
                    raise InvalidFileFormatError(file_name)
        except InvalidFileFormatError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)
        else:
            print(f"Songs loaded from {file_name}.\n")
    
    def view_song_database(self) -> None:
        """Displays the song database."""
        try:
            if not self.database:
                raise EmptyDatabaseException()
            print("\n")
            print("Songs Database:")
            print("{:<40} {:<20} {:<10}".format("Title", "Artist", "Genre"))
            print("=" * 70)
            for artist, songs in self.database.items():
                for song in songs:
                    try:
                        print("{:<40} {:<20} {:<10}".format(song.title, artist, song.genre))
                    except AttributeError as e:
                        print(f"Error displaying song: {e}")
                        continue
        except EmptyDatabaseException as e:
            print(e)
        finally:
            print("\n")

    def delete_song(self, artist: str, title: str) -> None:
        """Deletes a song from the database."""
        try:
            if not self.database:
                raise EmptyDatabaseException()
            for song in self.database[artist]:
                if song.title.lower() == title.lower():
                    old_entry = f"{song.title},{artist},{song.album},{song.genre},{song.duration}"
                    self.database[artist].remove(song)
                    if not self.database[artist]:
                        self.database.pop(artist)
                    delete_file_entry(self.file_path, self.database_file, old_entry)
                    print(f'Deleted "{title}" by "{artist}" from the database.')
                    return
            raise SongNotFoundException(title)
        except EmptyDatabaseException as e:
            print(e)
        except SongNotFoundException as e:
            print(e)
    
    def modify_song(self, artist: str, title: str) -> None:
        """Modifies a song in the database."""
        try:
            if not self.database:
                raise EmptyDatabaseException()
            for song in self.database[artist]:
                if song.title.lower() == title.lower():
                    print("Current details:")
                    print(f'Title: "{song.title}", Album: "{song.album}", Genre: "{song.genre}", Duration: "{song.duration}"')
                    
                    old_entry = f"{song.title},{artist},{song.album},{song.genre},{song.duration}"
                    new_album = input("Enter new album (or press Enter to keep current): ") or song.album
                    new_genre = input("Enter new genre (or press Enter to keep current): ") or song.genre
                    new_duration = input("Enter new duration (or press Enter to keep current): ") or song.duration

                    song.album = new_album
                    song.genre = new_genre
                    song.duration = new_duration

                    new_entry = f"{song.title},{artist},{song.album},{song.genre},{song.duration}"
                    update_file_entry(self.file_path, self.database_file, old_entry, new_entry)
                    print(f'Modified "{title}" by "{artist}".')
                    return
            raise SongNotFoundException(title)
        except EmptyDatabaseException as e:
            print(e)
        except SongNotFoundException as e:
            print(e)
    
    def get_valid_artist(self) -> str:
        """Prompts for and returns a valid artist name."""
        while True:
            artist = input("Enter the artist name: ")
            try:
                if self._is_valid_artist(artist):
                    return self._get_actual_artist_name(artist)
            except ArtistNotFoundException as e:
                print(e)
                print("Please try again.")
    
    def _is_valid_artist(self, artist: str) -> bool:
        """Checks if the artist exists in the database."""
        try:
            if artist.lower() not in [artist.lower() for artist in self.database]:
                raise ArtistNotFoundException(artist)
            return True
        except ArtistNotFoundException as e:
            print(e)
            return False
    
    def is_database_empty(self) -> bool:
        """Check if the database is empty."""
        return len(self.database) == 0

    
    def _get_actual_artist_name(self, artist: str) -> str:
        """Returns the actual artist name as stored in the database."""
        for db_artist in self.database:
            if db_artist.lower() == artist.lower():
                return db_artist
    
    def _add_song(self, song: Song) -> None:
        """Adds a song to the database."""
        if song.artist.lower() not in [artist.lower() for artist in self.database]:
            self.database[song.artist] = []
        self.database[song.artist].append(song)