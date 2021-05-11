###########################################################################
# Team Name: Chariot
# Date: 03/29/2021
# Description: Vigenere Cipher | Ver: 3.9
###########################################################################
import sys

# encrypts the text with the key using vigenere cipher
def encrypt(text, key):
    # text and key value represent the value of the letter in the alphabet
    text_value = 0
    key_value = 0

    # text and key index represent the index of the text and key
    text_index = 0
    key_index = 0

    # empty encrypted cipher string
    cipher = ""

    # if the text is longer than the key, make a new key with the same length as the text
    key = (key*len(text))[:len(text)]

    while(len(cipher) != len(text)):
        # if the character is not a letter, go to the next letter
        if(text[text_index].isalpha() == False):
            cipher += text[text_index]
            text_index += 1

        else:    
            # get the index of the character in the alphabet for the text and key
            text_value = alphabet.index((text[text_index]).lower())
            key_value = alphabet.index((key[key_index]).lower())

            # if the text letter is uppercase, convert to uppercase
            if(text[text_index].isupper()):
                cipher += alphabet[((text_value + key_value) % 26)].upper()
            else:
                cipher += alphabet[((text_value + key_value) % 26)]

            # increment the text and key index
            text_index += 1
            key_index += 1

    return cipher

# decrypt the text with the key using vigenere cipher
def decrypt(text, key):
    # text and key value represent the value of the letter in the alphabet
    text_value = 0
    key_value = 0

    # text and key index represent the index of the text and key
    text_index = 0
    key_index = 0

    # empty encrypted cipher string
    cipher = ""
    
    # if the text is longer than the key, make a new key with the same length as the text
    key = (key*len(text))[:len(text)]

    while(len(cipher) != len(text)):
        # if the character is not a letter, go to the next letter
        if(text[text_index].isalpha() == False):
            cipher += text[text_index]
            text_index += 1

        else:    
            # get the index of the character in the alphabet for the text and key
            text_value = alphabet.index((text[text_index]).lower())
            key_value = alphabet.index((key[key_index]).lower())

            # if the text letter is uppercase, convert to uppercase
            if(text[text_index].isupper()):
                cipher += alphabet[((26 + text_value - key_value) % 26)].upper()
            else:
                cipher += alphabet[((26 + text_value - key_value) % 26)]

            # increment the text and key index
            text_index += 1
            key_index += 1

    return cipher

############
### MAIN ###
############

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

try:
    key = (sys.argv[2]).replace(" ", "")
    if(sys.argv[1] == "-e"):
        for text in sys.stdin:
            text = text.strip('\n')
            print(encrypt(text, key))
            
    elif(sys.argv[1] == "-d"):
        for text in sys.stdin:
            text = text.strip('\n')
            print(decrypt(text, key))

except KeyboardInterrupt:
    quit()
