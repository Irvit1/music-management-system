"""
Create a class named SongsManagementSystemUser
    fetch the songs data in init method

    Create function load_song_data
    filename, filepath as input variables

    function search_song_by_title

    function search_songs_by_artist

"""

import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import read_file


class SongsManagementSystemUser:
    def __init__(self) -> None:
        self.database = {}
        self.file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../database/")
        self.songs_by_title = {}
        self.songs_by_artist = {}

    def load_song_data(self):
       
        try:
            song_data = read_file(self.file_path, "songs.txt")
            
            for line in song_data:
                data = line.strip().split(',')
                if len(data) == 5:
                    title, artist, album, genre, duration = [item.strip().lower() for item in data]
                    # Store by title for direct song search
                    self.songs_by_title[title] = (artist, album, genre, duration)
                    # Store by artist for easy retrieval of all songs by the artist
                    if artist not in self.songs_by_artist:
                        self.songs_by_artist[artist] = []
                    self.songs_by_artist[artist].append((title, album, genre, duration))

        except Exception as e:
            print(f"An unexpected error occurred while loading the data: {e}")

    def search_song(self):
        """Search for a song by title."""
        try:
            song_name = input("Enter Song Name : ").strip().lower()

            if song_name in self.songs_by_title:
                artist, album, genre, duration = self.songs_by_title[song_name]
                print(f"Searching songs with title : {song_name}")
                print(f"Found : {song_name} by {artist} (Album: {album}, Genre: {genre}, Duration: {duration})")
            else:
                print("Song not found")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def same_artist_songs(self):
        """List all songs by a given artist."""
        try:
            artist_name = input("Enter Artist Name : ").strip().lower()

            if artist_name in self.songs_by_artist:
                print(f"Songs by {artist_name.capitalize()}:")
                for title, album, genre, duration in self.songs_by_artist[artist_name]:
                    print(f"Found : {title} (Album: {album}, Genre: {genre}, Duration: {duration})")
            else:
                print("No songs available from this artist")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
