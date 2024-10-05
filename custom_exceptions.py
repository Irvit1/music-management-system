class FileNotFoundErrorCustom(Exception):
    """Custom exception raised when a file is not found."""
    def __init__(self, file_name):
        super().__init__(f"Error: File '{file_name}' not found in the specified path.")

class InvalidFileFormatError(Exception):
    """Custom exception raised when the file format is incorrect."""
    def __init__(self, file_name):
        super().__init__(f"Error: Invalid format in file '{file_name}'. Please ensure it has the correct format (title, artist, album, genre, duration).")

class SongNotFoundException(Exception):
    """Custom exception raised when a song is not found."""
    def __init__(self, song_name):
        super().__init__(f"Error: Song '{song_name}' not found.")

class ArtistNotFoundException(Exception):
    """Custom exception raised when an artist is not found."""
    def __init__(self, artist_name):
        super().__init__(f"Error: Artist '{artist_name}' not found.")

class EmptyDatabaseException(Exception):
    def __init__(self):
        super().__init__("The song database is empty.")
