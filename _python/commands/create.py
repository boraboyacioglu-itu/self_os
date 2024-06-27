import os
import curses

from apps.editor import run as editor

__doc__ = "Creates a new file with the given content. Usage: create <filename>"

def run(dir, *args):
    """ Creates a new file with the given content. """
    
    # Check if a filename provided.
    if not args:
        return "Error: No filename provided.", True

    # Get the filename.
    filename = args[0]
    filepath = os.path.join(dir, filename)
    
    # Check if the file already exists.
    if os.path.exists(filepath):
        return f"Error: File '{filename}' already exists.", True
    
    content = editor([' '])
    
    # Write the content to the file.
    with open(filepath, 'w') as file:
        file.write('\n'.join(content))
        
    return f"File '{filename}' created.", False
    