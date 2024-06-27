from importlib import util
import os
import readline

class SelfTerminal:
    def __init__(self):
        # Set the version.
        self.version = '0.1'
        
        # Set the current directory.
        self.dir = os.getcwd()
        
        # Get the available commands.
        self.commands = {}
        self.helps = {}
        self.load_commands()
        
        self.load_history()
        
    def load_commands(self):
        """ Loads the possible commands from the commands directory. """
        
        # Get the list of files in the commands directory.
        files = os.listdir('commands')
        
        # Load each command.
        for file in files:
            # Skip non-python-function files.
            if not file.endswith('.py') or file == '__init__.py':
                continue
            
            # Load the command.
            name = file[:-3]
            path = f'commands/{file}'
            spec = util.spec_from_file_location(name, path)
            module = util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Add the command to the dictionary.
            self.commands[name] = module
            self.helps[name] = module.__doc__
    
    def run_command(self, command):
        """ Runs the given command. """
        
        # Get the command name and arguments.
        parts = command.split()
        name = parts[0]
        args = parts[1:]
        
        if name == 'help':
            # Print the list of commands.
            max_len = max(len(name) for name in self.commands)
            commands = sorted(self.commands)
            for name in commands:
                print(f"\033[93m{name:<{max_len}}\033[0m : {self.helps[name]}")
            return
        
        # Check if the command is valid.
        if name not in self.commands:
            print(f"\033[91mCommand '{name}' not found.\033[0m")
            return
        
        # Run the command.
        result, err = self.commands[name].run(self.dir, *args)
        
        # Update the directory if the command is 'cd'.
        if name == 'cd' and not err:
            self.dir = os.path.abspath(result)
            result = ''
        
        if result:
            color = '\033[91m' if err else '\033[92m'
            print(f"{color}{result}\033[0m")
            
    def run(self):
        """ Runs the terminal. """
        
        # Print the welcome message.
        print(f"\nWelcome to SelfOS {self.version}!",
              "This is a simple terminal-based operating system. It replicates DOS on Python.",
              "Type \033[93m'help'\033[0m for a list of commands.",
              sep='\n')
        
        # Run the terminal.
        while True:
            # Get the command.
            command = input(f"\n\033[2m{self.dir}>\033[0m ")
            
            # Check if the command is empty.
            if not command.strip():
                continue
            
            # Check if the command is 'exit'.
            if command == 'exit':
                break
            
            # Run the command.
            self.run_command(command)
        
        print("")
        self.save_history()
            
    def save_history(self):
        """ Saves the history of the terminal. """
        
        # Get the history file path.
        history_path = os.path.join(self.dir, '.selfos_history')
        
        # Save the history.
        readline.write_history_file(history_path)
    
    def load_history(self):
        """ Loads the history of the terminal. """
        
        # Get the history file path.
        history_path = os.path.join(self.dir, '.selfos_history')
        
        # Load the history.
        if os.path.exists(history_path):
            readline.read_history_file(history_path)