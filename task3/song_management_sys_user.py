"""
Create a class named SongsManagementSystemUser
    fetch the songs data in init method

    Create function load_song_data
    filename, filepath as input variables

    function search_song_by_title

    function search_songs_by_artist

"""

from task2.song_management_sys import SongsManagementSystem

class SongManagementSystemUser(SongsManagementSystem):
    # fetch song data in init method
    def __init__(self, filename: str) -> None:
        super().__init__()
        # Implement a try except in init method and raise FileNotFoundErrorCustom exception if file is not found or InvalidFileFormatError if file format is incorrect
        self.load_song_data(filename)

    # search song by title
    def search_song_by_title(self, title: str) -> None:
        # Implement a try except in this function and raise SongNotFoundException if song is not found
        # In try, if the result is available, print the result
        print('temp')
    

    def search_songs_by_artist(self, artist: str) -> None:
        # Implement a try except in this function and raise ArtistNotFoundException if artist is not found
        # In try, if the result is available, return the result
        print('temp')




    
