"""
Create a SONG class having following fields
title, artist, album, genre, duration
"""

# it contains only the model class
class Song:
    def __init__(self, title: str, artist: str, album: str, genre: str, duration: str):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.duration = duration

    def __eq__(self, other):
        if not isinstance(other, Song):
            return None
        return (self.title, self.artist, self.album) == (other.title, other.artist, other.album)

    def __hash__(self):
        return hash((self.title, self.artist, self.album))