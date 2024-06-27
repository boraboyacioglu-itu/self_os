import os

__doc__ = "Removes the given directory. Usage: rmdir <dirname>"

def run(dir, *args):
    """ Removes the given directory. """
    
    # Check if a directory name provided.
    if not args:
        return "Error: No directory name provided.", True

    # Get the directory name.
    dirname = args[0]
    dirpath = os.path.join(dir, dirname)
    
    # Check if the directory exists.
    if not os.path.exists(dirpath):
        return f"Error: Directory '{dirname}' not found.", True
    
    # Remove the directory.
    os.rmdir(dirpath)
    return f"Directory '{dirname}' removed.", False