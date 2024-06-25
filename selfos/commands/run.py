from importlib import util
import os

import curses

__doc__ = "Runs an application. Usage: run <appname>"

def run(dir, *args):
    """ Runs an application. """
    
    # Load the app from the apps directory.
    path = os.path.join('apps', args[0] + '.py')
    spec = util.spec_from_file_location(args[0], path)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Run the app.
    string = curses.wrapper(module.run, dir, *args[1:])
    
    return string, False