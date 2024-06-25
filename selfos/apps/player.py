import os
import curses
import pygame

def run(stdscr, dir, *args):
    music_file = os.path.join(args[0])
    
    curses.curs_set(0)
    stdscr.clear()
    pygame.mixer.init()
    
    if not os.path.exists(music_file):
        stdscr.addstr(0, 0, f"Error: '{music_file}' does not exist.")
        stdscr.refresh()
        stdscr.getch()
        return
    
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()

    stdscr.addstr(0, 0, f"Playing '{music_file}'")
    stdscr.addstr(1, 0, "Press 'p' to pause, 'r' to resume, 's' to stop, and 'q' to quit.")
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key == ord('p'):
            pygame.mixer.music.pause()
            stdscr.addstr(2, 0, "Paused")
        elif key == ord('r'):
            pygame.mixer.music.unpause()
            stdscr.addstr(2, 0, "Resumed")
        elif key == ord('s'):
            pygame.mixer.music.stop()
            stdscr.addstr(2, 0, "Stopped")
        elif key == ord('q'):
            pygame.mixer.music.stop()
            break
        stdscr.refresh()

    pygame.mixer.quit()
    return f"Playing '{args[0]}'"