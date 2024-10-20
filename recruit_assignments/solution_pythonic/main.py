import sys
import os
from logic import core_logic_func


def main():
    if len(sys.argv) != 3:
        print("Usage: program message.txt magazine.txt")
        return 1 

    message_file = sys.argv[1]
    magazine_file = sys.argv[2]

    try:
        if not os.path.exists(message_file):
            print(f"Error: '{message_file}' not found.")
            return 1

        with open(message_file, 'r') as f:
            message = f.read()
        if not os.path.exists(magazine_file):
            print(f"Error: '{magazine_file}' not found.")
            return 1

        with open(magazine_file, 'r') as f:
            magazine = f.read()

        if not message.strip():
            print("Error: The message file is empty.")
            return 1

        if not magazine.strip():
            print("Error: The magazine file is empty.")
            return 1

    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return 1

    except PermissionError as e:
        print(f"Permission denied: {e}")
        return 1

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 1


    result = core_logic_func(message, magazine)
    print("Can construct ransom message:", result)



if __name__ == "__main__":
    main()
