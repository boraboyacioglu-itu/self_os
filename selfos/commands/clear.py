import os

__doc__ = "Clears the screen. Usage: clear"

def run(dir, *args):
    """ Clears the screen. """
    
    # Clear the screen.
    os.system('cls' if os.name == 'nt' else 'clear')
    return '', False