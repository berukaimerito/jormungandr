#!/usr/bin/env python3
'''
program.py Friday 18 Oct
#receives cli arguments
#take the input from the user
#search for the files in the root directory
#send data to the logic functions, receive the result
#print result to the terminal
#
# def cli_run(args):
#     # if it includes message.txt and magazinte.txt with split func.
#     # start reading it
#     pass

# def parse_txt():
#     # parse txt and stores it in associated data structure
#     # pass data structures into the core logic.
#     pass
# how many edge cases i should think here?
# enough tinkering, time to code.
'''

import sys
from solution_python.logic import core_logic_func

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