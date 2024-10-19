import sys
from logic import core_logic_func

def main():
    if len(sys.argv) != 3:
        print("Usage: program message.txt magazine.txt")
    message_file = sys.argv[1]
    magazine_file = sys.argv[2]

    with open(message_file, 'r') as f:
        message = f.read()
    with open(magazine_file, 'r') as f:
        magazine = f.read()

    # calling core logic function
    result = core_logic_func(message, magazine)
    print("Can construct ransom message: ", result)

if __name__ == "__main__":
    main()