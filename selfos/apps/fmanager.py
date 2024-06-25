import os
import curses

def list_dir(stdscr, current_dir, i):
    stdscr.clear()
    files = os.listdir(current_dir)
    files.insert(0, "..")  # Add option to go up one level
    for j, file in enumerate(files):
        if j == i:
            stdscr.addstr(j, 0, file, curses.A_REVERSE)
        else:
            stdscr.addstr(j, 0, file)
    stdscr.addstr(len(files) + 1, 0, "Use arrow keys to navigate, Enter to select, 'q' to quit, 'v' to view file.")
    stdscr.refresh()
    return files

def view_file(stdscr, file_path):
    stdscr.clear()
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    max_y, max_x = stdscr.getmaxyx()
    line_num = 0
    while True:
        stdscr.clear()
        for j, line in enumerate(lines[line_num:line_num + max_y - 1]):
            stdscr.addstr(j, 0, line[:max_x])
        stdscr.addstr(max_y - 1, 0, "Press 'q' to return.")
        stdscr.refresh()
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == curses.KEY_UP and line_num > 0:
            line_num -= 1
        elif key == curses.KEY_DOWN and line_num < len(lines) - max_y:
            line_num += 1

def file_manager(stdscr, dir):
    curses.curs_set(0)
    i = 0

    while True:
        files = list_dir(stdscr, dir, i)
        key = stdscr.getch()
        
        if key == curses.KEY_UP:
            i = max(0, i - 1)
        elif key == curses.KEY_DOWN:
            i = min(len(files) - 1, i + 1)
        elif key == curses.KEY_ENTER or key == ord('\n'):
            selected_file = files[i]
            selected_path = os.path.join(dir, selected_file)
            if selected_file == "..":
                dir = os.path.dirname(dir)
                i = 0
            elif os.path.isdir(selected_path):
                dir = selected_path
                i = 0
            else:
                stdscr.addstr(len(files) + 1, 0, f"'{selected_file}' is a file. Press 'v' to view or any other key to continue.")
                stdscr.refresh()
                key = stdscr.getch()
                if key == ord('v'):
                    view_file(stdscr, selected_path)
        elif key == ord('q'):
            break
    
    return ''

def run(dir, *args):
    """ Opens a file manager to navigate directories. """
    return curses.wrapper(file_manager, dir)