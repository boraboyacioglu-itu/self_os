import os

__doc__ = "Shows the content of the given file. Usage: show <filename> [lines]"

def run(dir, *args):
    """ Shows the content of the given file. """
    
    # Check if a filename provided.
    if not args:
        return "Error: No filename provided.", True

    # Get the filename.
    filename = args[0]
    filepath = os.path.join(dir, filename)
    
    # Get the number of lines to show.
    lines = int(args[1]) if len(args) > 1 else None
    
    # Check if the file exists.
    if not os.path.exists(filepath):
        return f"Error: File '{filename}' not found.", True
    
    # Read the content of the file.
    with open(filepath, 'r') as file:
        content = list(file.readlines())
        
    # Show the content.
    for i, line in enumerate(content[:lines]):
        print(f"{i:2d}:  {line}", end='')
    
    return '', False