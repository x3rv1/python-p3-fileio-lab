# lib/file_io.py

def write_file(file_name, file_content):
    """
    Writes content to a .txt file.
    Overwrites the file if it already exists.
    """
    with open(f"{file_name}.txt", "w", encoding="utf-8") as f:
        f.write(file_content)


def append_file(file_name, append_content):
    """
    Appends content to a .txt file.
    Creates the file if it does not exist.
    """
    with open(f"{file_name}.txt", "a", encoding="utf-8") as f:
        f.write(append_content)


def read_file(file_name):
    """
    Reads and returns the content of a .txt file.
    """
    with open(f"{file_name}.txt", "r", encoding="utf-8") as f:
        return f.read()