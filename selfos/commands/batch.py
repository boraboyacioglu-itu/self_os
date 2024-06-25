import os

__doc__ = "Runs a batch file. Usage: batch <filename>"

def run(dir, *args):
    """ Runs a batch file. """
    
    # Check if a filename provided.
    if not args:
        return "Error: No filename provided.", True

    # Get the filename.
    filename = args[0]
    filepath = os.path.join(dir, filename)
    
    # Check if the file exists.
    if not os.path.exists(filepath):
        return f"Error: File '{filename}' not found.", True
    
    # Run the batch file.
    os.system(filepath)
    return '', False