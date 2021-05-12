##############################################################################
# Name: Team Chariot- Ahmed Mudhish, Andre Caver, Avery Miller, Brianna Stewart
# Garrett Gresham, Kevin Oubre, Sydney Holland
# Date: 05/07/2021
# Description: 06- XOR Program | Ver: 3.8.5
##############################################################################
import sys

KEY_FILE_NAME = "challenge"

# A function that takes a message and key and XOR's each bit of m with k.
def xor(message, key):
    message_bytearray = bytearray(message)
    key_bytearray = bytearray(key)
    encrypted_bytearray = bytearray()

    # Check the lengths of message and key to ensure they are equal.
    if(len(message_bytearray) > len(key_bytearray)):
        count = 0
        new_key_bytearray = bytearray()
        while(len(message_bytearray) != len(new_key_bytearray)):
            if(count == len(key_bytearray)):
                count = 0
            new_key_bytearray.append(message_bytearray[count])
            count += 1

    # Iterate through each byte and store the XOR'd result in a bytearray.
    for byte in range(len(message_bytearray)):
        encrypted_bytearray.append(message_bytearray[byte] ^ key_bytearray[byte])

    return encrypted_bytearray
        
# Main function of the program.
def main():
    # Read the key from the current directory.
    with open(KEY_FILE_NAME, "rb") as file:
        key = file.read()

    # Read the plaintext or ciphertext from stdin.
    message = sys.stdin.buffer.read()

    # Send the generated output to stdout.
    sys.stdout.buffer.write(xor(message, key))

if __name__ == "__main__":
    main()