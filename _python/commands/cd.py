import os

__doc__ = "Changes the current directory. Usage: cd <dirname>"

def run(dir, *args):
    """ Changes the current directory. """
    
    # Check if a directory name provided.
    if not args:
        return "Error: No directory name provided.", True

    # Get the directory name.
    dirname = args[0]
    dirpath = os.path.join(dir, dirname)
    
    # Check if the directory exists.
    if not os.path.exists(dirpath):
        return f"Error: Directory '{dirname}' not found.", True
    
    return dirpath, False