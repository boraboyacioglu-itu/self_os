import os

__doc__ = "Deletes the given file. Usage: del <filename>"

def run(dir, *args):
    """ Deletes the given file. """
    
    # Check if a filename provided.
    if not args:
        return "Error: No filename provided.", True

    # Get the filename.
    filename = args[0]
    filepath = os.path.join(dir, filename)
    
    # Check if the file exists.
    if not os.path.exists(filepath):
        return f"Error: File '{filename}' not found.", True
    
    # Delete the file.
    os.remove(filepath)
    return f"File '{filename}' deleted.", False