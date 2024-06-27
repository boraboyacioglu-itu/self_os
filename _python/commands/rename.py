import os

__doc__ = "Renames the given file. Usage: rename <filename> <newname>"

def run(dir, *args):
    """ Renames the given file. """
    
    # Check if a filename provided.
    if len(args) < 2:
        return "Error: No filename or new name provided.", True

    # Get the filename and new name.
    filename = args[0]
    newname = args[1]
    filepath = os.path.join(dir, filename)
    newpath = os.path.join(dir, newname)
    
    # Check if the file exists.
    if not os.path.exists(filepath):
        return f"Error: File '{filename}' not found.", True
    
    # Check if the new name already exists.
    if os.path.exists(newpath):
        return f"Error: File '{newname}' already exists.", True
    
    # Rename the file.
    os.rename(filepath, newpath)
    return f"File '{filename}' renamed to '{newname}'. Note that you may need to restart the system for the changes to take effect.", False