import os

__doc__ = "Finds the given string under all files in the current or given directory. Usage: find <string> [dir]"

def run(dir, *args):
    """ Finds the given string under all files in the current or given directory. """
    
    # Check if a string provided.
    if not args:
        return "Error: No string provided.", True

    # Get the string.
    string = args[0]
    
    dir = dir if not args[1:] else args[1]
    
    # Find the string.
    finds = []
    for root, _, files in os.walk(dir):
        for file in files:
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                try:
                    content = f.read()
                    if string in content:
                        finds.append(f"{filepath}:{content.index(string)}")
                except UnicodeDecodeError:
                    pass
    
    if finds:
        return '\n'.join(finds), False
    
    return f"Error: String '{string}' not found.", True