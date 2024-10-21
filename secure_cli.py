import os
import sys


USERNAME = "admin"
PASSWORD = "password123"

def authenticate():
    """Prompt the user for a username and password and authenticate them."""
    print("Please log in to access the shell.")
    username = input("Username: ")
    password = input("Password: ")
    
    if username == USERNAME and password == PASSWORD:
        print("Authentication successful!")
    else:
        print("Authentication failed. Exiting...")
        sys.exit(1)

def list_directory():
    """List the contents of the current directory."""
    current_directory = os.getcwd()
    files = os.listdir(current_directory)
    print("Contents of the current directory:")
    for file in files:
        print(file)

def add_numbers(a, b):
    """Add two numbers and print the result."""
    result = a + b
    print(f"Result: {result}")

def show_help():
    """Display available commands."""
    print("Available commands:")
    print("LIST - List the contents of the current directory")
    print("ADD a b - Add two numbers together (a and b)")
    print("HELP - Show the list of available commands")
    print("EXIT - Exit the shell")

def main():
    """Main loop to execute commands."""
    authenticate()  # Call authentication function at the start

    print("Welcome to the Python Shell! Type HELP for commands.")
    while True:
        command = input("Enter a command: ").strip()
        
        if not command:  # Check for empty input
            print("Please enter a command.")
            continue
        
        command_parts = command.split()
        command_upper = command_parts[0].upper()

        if command_upper == "LIST":
            list_directory()
        elif command_upper == "ADD":
            if len(command_parts) == 3:
                try:
                    a = float(command_parts[1])
                    b = float(command_parts[2])
                    add_numbers(a, b)
                except ValueError:
                    print("Invalid input. Please provide two numbers.")
            else:
                print("Invalid input. ADD command expects two numbers.")
        elif command_upper == "HELP":
            show_help()
        elif command_upper == "EXIT":
            print("Exiting shell...")
            sys.exit(0)
        else:
            print("Invalid command. Type HELP for a list of available commands.")

if __name__ == "__main__":
    main()
