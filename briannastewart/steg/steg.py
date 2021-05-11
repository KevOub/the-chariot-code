##############################################################################
# Name: Brianna Stewart
# Date: 05/05/2021
# Description: 06- XOR Program | Ver: 3.8.5
##############################################################################
import sys
from math import floor

SENTINEL = ""
STORING_METHOD = ""

# Byte Method
def byte_method():
    pass

# Bit Method
def bit_method():
    pass

# Main function of the program.
def main():
    # Read the terminal arguments.
    arguments = []

    if(sys.argv[1] == "-s"):
        print("store")
        if(sys.argv == "-b"):
            print("bit store")
        elif(sys.argv == "-B"):
            print("byte store")
    
    # arguments = {
    #     "-s": "store",
    #     "-r": "retrieve",
    #     "-b": "bit mode",
    #     "-B": "byte mode" 
    # }
    # print(arguments.get(sys.argv[1], "default"))

    # Read the wrapper data from a file as binary data.

    # Read the hidden data (if applicable) from a file as binary data.

    # Detect if either file is not found and provide an error message.

    # Write the result to stdout as binary data.

    pass

if(__name__ == "__main__"):
    main()