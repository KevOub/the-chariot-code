###########################################################################
# Name: Brianna Stewart
# Date: 03/25/2021
# Description: 01- Binary Decoder | Ver: 3.8.5
###########################################################################
import sys

# A function that determines whether the message is 7-bit or 8-bit binary.
def checkLength(num):
    if (num % 8 == 0):
        return 8
    else:
        return 7

def string_to_list(message):
    li = []
    length = len(message)
    if (checkLength(length) == 7):
        for x in range(0, length, 7):
            li.append(message[x:x+7])
    else:
        for x in range(0, length, 8):
            li.append(message[x:x+8])

    return li

def convert_to_decimal(li):
    converted_list = []
    for x in range(len(li)):
        converted_list.append(int(li[x], 2))

    return converted_list

def decimal_to_ascii(li):
    message = ""
    for x in li:
        message += chr(x)

    return message

def main():
    # stores the binary code from the input file, stripping the white space
    binary = (sys.stdin.read()).rstrip()
    binary_list = string_to_list(binary)
    decimal_list = convert_to_decimal(binary_list)
    message = decimal_to_ascii(decimal_list)
    print(message)

if(__name__ == "__main__"):
    main()