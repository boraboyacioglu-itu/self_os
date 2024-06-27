import os

__doc__ = "Creates a new directory. Usage: mkdir <dirname>"

def run(dir, *args):
    """ Creates a new directory. """
        
    # Check if a directory name provided.
    if not args:
        return "Error: No directory name provided.", True

    # Get the directory name.
    dirname = args[0]
    dirpath = os.path.join(dir, dirname)
    
    # Check if the directory already exists.
    if os.path.exists(dirpath):
        return f"Error: Directory '{dirname}' already exists.", True
    
    # Create the directory.
    os.mkdir(dirpath)
    return f"Directory '{dirname}' created.", False