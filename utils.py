"""
is_valid_email()
password checker
read file function 
write file function

"""

from custom_exceptions import FileNotFoundErrorCustom
import os

def read_file(file_path: str, file_name: str) -> list:
    """Reads the content of a file located at `file_path/file_name`."""
    try:
        with open(os.path.join(file_path, file_name), 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        raise FileNotFoundErrorCustom(file_name)
    except IOError as e:
        raise IOError(f"Error reading file '{file_name}': {str(e)}")

def write_file(file_path: str, file_name: str, data: list) -> None:
    """Writes data to a file at `file_path/file_name`."""
    try:
        with open(os.path.join(file_path, file_name), 'w') as file:
            file.writelines(data)
    except IOError as e:
        raise IOError(f"Error writing to file '{file_name}': {str(e)}")

def update_file_entry(file_path: str, file_name: str, old_entry: str, new_entry: str) -> None:
    """Updates a specific entry in the file."""
    try:
        lines = read_file(file_path, file_name)
        updated_lines = [new_entry + '\n' if line.strip() == old_entry else line for line in lines]
        write_file(file_path, file_name, updated_lines)
    except (FileNotFoundErrorCustom, IOError) as e:
        raise IOError(f"Error updating entry in file '{file_name}': {str(e)}")

def delete_file_entry(file_path: str, file_name: str, entry_to_delete: str) -> None:
    """Deletes a specific entry from the file."""
    try:
        lines = read_file(file_path, file_name)
        updated_lines = [line for line in lines if line.strip() != entry_to_delete.strip()]
        write_file(file_path, file_name, updated_lines)
    except (FileNotFoundErrorCustom, IOError) as e:
        raise IOError(f"Error deleting entry from file '{file_name}': {str(e)}")