import psutil

def list_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}")

def task_manager():
    while True:
        print("\nTask Manager")
        print("1. List Processes")
        print("2. Kill Process")
        print("3. Quit")
        choice = input("Enter choice: ")

        if choice == '1':
            list_processes()
        elif choice == '2':
            pid = int(input("Enter PID to kill: "))
            try:
                proc = psutil.Process(pid)
                proc.terminate()
                print(f"Process {pid} terminated.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

def run(dir, *args):
    task_manager()
    return ''
