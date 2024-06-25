import os
import time

__doc__ = "Shows the information about a file or directory. Usage: info <filename>"

def run(dir, *args):
    """ Shows the information about a file or directory. """
        
    # Check if a filename provided.
    if not args:
        return "Error: No filename provided.", True

    # Get the filename.
    filename = args[0]
    filepath = os.path.abspath(os.path.join(dir, filename))
    
    # Check if the file exists.
    if not os.path.exists(filepath):
        return f"Error: File '{filename}' not found.", True
    
    # Get the information about the file.
    info = os.stat(filepath)
    size = info.st_size
    ctime = time.ctime(info.st_ctime)
    mtime = time.ctime(info.st_mtime)
    
    print(
        f"Name     : {filename}",
        f"Path     : {filepath}",
        f"Size     : {size} bytes",
        f"Created  : {ctime}",
        f"Modified : {mtime}",
        sep='\n'
    )
    
    return '', False