import os
import time

__doc__ = "Lists the files in the current directory. Usage: ls [directory]"

def run(dir, *args):
    """ Lists the files in the current directory. """
    
    # Check if a directory name provided.
    if args:
        dir = os.path.join(dir, args[0])
    
    # Get the files in the directory.
    files = os.listdir(dir)
    
    # Check if there are any files.
    if not files:
        print("No files found.")
        
    titles = ['Filename', 'Size', 'Created', 'Modified']
        
    # Get the file information.
    detailed = [
        [filename,
         str(os.stat(os.path.join(dir, filename)).st_size),
         time.ctime(os.path.getctime(os.path.join(dir, filename))),
         time.ctime(os.path.getmtime(os.path.join(dir, filename)))]
        for filename in files
    ]
    
    # Print the files.
    max_lens = [
        max(len(file[i]) for file in detailed + [titles])
        for i in range(len(detailed[0]))
    ]
    
    print(' | '.join(f"\033[1m{title:<{max_len}}\033[0m" for title, max_len in zip(titles, max_lens)))
    print('-|-'.join('-' * max_len for max_len in max_lens))
    for file in detailed:
        print(' | '.join(file[i].ljust(max_len) for i, max_len in enumerate(max_lens)))
    
    return '', False