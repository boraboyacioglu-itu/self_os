import os

__doc__ = "Copies the given file. Usage: copy <source> <destination>"

def run(dir, *args):
    """ Copies the given file. """
    
    # Check if a source and destination provided.
    if len(args) < 2:
        return "Error: No source or destination provided.", True

    # Get the source and destination.
    src = os.path.join(dir, args[0])
    dst = os.path.join(dir, args[1])
    
    # Check if the source file exists.
    if not os.path.exists(src):
        return f"Error: File '{args[0]}' not found.", True
    
    # Check if the destination file already exists.
    if os.path.exists(dst):
        return f"Error: File '{args[1]}' already exists.", True
    
    # Copy the file.
    with open(src, 'rb') as fsrc:
        with open(dst, 'wb') as fdst:
            fdst.write(fsrc.read())
    
    return f"File '{args[0]}' copied to '{args[1]}'.", False