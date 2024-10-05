"""
Create a SONG class having following fields
title, artist, album, genre, duration
"""

class Song:
    def __init__(self, title: str, artist: str, album: str, genre: str, duration:str) -> None:
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.duration = duration