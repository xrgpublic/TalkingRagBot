
def read_python_file(filename):
    """
    Read the contents of a Python file.

    Args:
        filename (str): The name of the Python file to be read.

    Returns:
        str: The contents of the Python file as a string.
    """
    try:
        with open(filename, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None

def readFile():
    filename = input("Enter the name of the Python file to read (e.g., myscript.py): ")
    code = read_python_file(filename)
    if code:
        print("The contents of the file are:")
        print(code)