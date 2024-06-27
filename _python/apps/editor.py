import curses

def editor(stdscr, content):
    """ The editor. """
    # Initialize the cursor position.
    y, x = 0, 0

    # Ensure the terminal is set to use UTF-8 encoding.
    curses.curs_set(1)
    
    # Main loop.
    while True:
        # Clear the screen.
        stdscr.clear()
        
        # Print the content.
        for i, line in enumerate(content):
            stdscr.addstr(i, 0, line.encode('utf-8').decode('utf-8'))
        
        # Add the instruction at the bottom of the screen.
        instruction = "Press Ctrl+X to exit"
        stdscr.addstr(curses.LINES - 1, 0, instruction)
        
        # Print the cursor.
        stdscr.move(y, x)
        
        # Refresh the screen.
        stdscr.refresh()
        
        # Get the key.
        key = stdscr.get_wch()
        
        # Handle the key.
        if key == curses.KEY_UP:
            y = max(y - 1, 0)
        elif key == curses.KEY_DOWN:
            y = min(y + 1, len(content) - 1)
        elif key == curses.KEY_LEFT:
            x = max(x - 1, 0)
        elif key == curses.KEY_RIGHT:
            x = min(x + 1, len(content[y]) if y < len(content) else 0)
        elif key == '\n':  # Enter key to add new line
            content.insert(y + 1, content[y][x:])
            content[y] = content[y][:x]
            y += 1
            x = 0
        elif key == '\x7f':  # Backspace key
            if x == 0:
                if y == 0:
                    continue
                x = len(content[y - 1])
                content[y - 1] += content[y]
                del content[y]
                y -= 1
            else:
                content[y] = content[y][:x - 1] + content[y][x:]
                x -= 1
        elif key == '\x18':  # Ctrl+X to exit
            break
        else:
            content[y] = content[y][:x] + key + content[y][x:]
            x += 1
    
    return content

def run(content):
    """ Runs the editor. """
    return curses.wrapper(editor, content)