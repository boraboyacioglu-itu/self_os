from main import SelfTerminal

if __name__ == '__main__':
    terminal = SelfTerminal()
    
    try:
        terminal.run()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)