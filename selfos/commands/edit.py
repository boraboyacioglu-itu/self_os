import os
import curses

from apps.editor import editor

__doc__ = "Edits the given file. Usage: edit <filename>"

def run(dir, *args):
    """ Edits the given file. """
        
    # Check if a filename provided.
    if not args:
        return "Error: No filename provided.", True

    # Get the filename.
    filename = args[0]
    filepath = os.path.join(dir, filename)
    
    # Check if the file exists.
    if not os.path.exists(filepath):
        return f"Error: File '{filename}' not found.", True
    
    # Open the file.
    with open(filepath, 'r') as file:
        content = file.readlines()
    
    # Edit the content.
    output = curses.wrapper(editor, content)
    
    # Save the content.
    with open(filepath, 'w') as file:
        file.write(''.join(output))
        
    return f"File '{filename}' saved.", False