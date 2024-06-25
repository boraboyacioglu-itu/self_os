import os

__doc__ = "Searches for a file under the current directory and its subdirectories. Usage: search <filename>"

def run(dir, *args):
    """ Searches for a file under the current directory and its subdirectories. """
    
    # Check if a filename provided.
    if not args:
        return "Error: No filename provided.", True

    # Get the filename.
    filename = args[0]
    
    # Search for the file.
    for root, _, files in os.walk(dir):
        if filename in files:
            return os.path.join(root, filename), False
    
    return f"Error: File '{filename}' not found.", True