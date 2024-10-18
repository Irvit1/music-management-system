"""
Create a class named SongsManagementSystemUser
    fetch the songs data in init method

    Create function load_song_data
    filename, filepath as input variables

    function search_song_by_title

    function search_songs_by_artist

"""



from custom_exceptions import ArtistNotFoundException, SongNotFoundException
from task2.song_management_sys import SongsManagementSystem

class SongManagementSystemUser(SongsManagementSystem):
    # fetch song data in init method
    def __init__(self, filename: str) -> None:
        super().__init__()
        # Implement a try except in init method and raise FileNotFoundErrorCustom exception if file is not found or InvalidFileFormatError if file format is incorrect
        try:
            self.load_song_data(filename)
        except FileNotFoundError as e:
            print(e)

    # search song by title
    def search_song_by_title(self, title: str) -> None:
        # Implement a try except in this function and raise SongNotFoundException if song is not found
        # In try, if the result is available, print the result
        try:
            found = False
            for artist, songs in self.database.items():
                for song in songs:
                    if song.title == title:
                        print(f"Searching songs with title: {title}")
                        print(f"Found: {song.title} by {artist} (Album: {song.album}, Genre: {song.genre}, Duration: {song.duration})")
                        found = True
                        break
                if found:
                    break
            if not found:
                raise SongNotFoundException(title)
        except SongNotFoundException as e:
            print(e)
    

    def search_songs_by_artist(self, artist: str) -> None:
        # Implement a try except in this function and raise ArtistNotFoundException if artist is not found
        # In try, if the result is available, return the result
        try:
            if artist in self.database:
                print(f"Searching songs by artist: {artist}")
                for song in self.database[artist]:
                    print(f"Found: {song.title} by {artist} (Album: {song.album}, Genre: {song.genre}, Duration: {song.duration})")
            else:
                raise ArtistNotFoundException(artist)
        except ArtistNotFoundException as e:
            print(e)




    
