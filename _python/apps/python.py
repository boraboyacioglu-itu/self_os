import sys
import io

def python(args):
    """Runs the given Python code."""
    # Create a buffer to capture stdout
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    
    try:
        # Try to evaluate the code (expressions)
        result = eval(args)
        if result is not None:
            print(result)
    except SyntaxError:
        # If it's a SyntaxError, it might be a statement, so exec it
        try:
            exec(args)
        except Exception as e:
            # Print exceptions in red
            print(f"\033[91m{e}\033[0m")
    except Exception as e:
        # Print exceptions in red
        print(f"\033[91m{e}\033[0m")
    finally:
        # Restore stdout
        sys.stdout = old_stdout
    
    # Get the output from the buffer and print it
    out = new_stdout.getvalue()
    if out:
        print(out)

def run(dir, *args):
    """ Runs the Python application in loop. """
    
    while True:
        try:
            # Get the user input.
            code = input('\033[94m>>> \033[0m')
            
            # Check if the user wants to exit.
            if code == 'exit()':
                raise EOFError()
            
            # Run the Python code.
            python(code)
        except EOFError:
            break