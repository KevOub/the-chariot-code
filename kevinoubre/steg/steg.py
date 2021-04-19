
import os
import sys
from math import floor

SENTINEL = [0x0,0xff,0x0,0xff,0x0]


""" 
python Steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]
"""

def loadfiles(file):
    with open(file, "rb") as f:
        return f.read()

def checkSentinel(mode,arr):
    # mode:True = right to left 
    if mode:
        if len(arr) != len(SENTINEL):
            return False
        g2g = [True if val == arr[count] else False for count,val in enumerate(SENTINEL)]
        return all(g2g)
            
    
    # left to right
    else:
        pass


class Steg():
    """ 
    s/r mode is either store or retrieve: True is store, False is retrieve
    b/B mode is either bit or Byte: True is bit, False is Byte
    """
    def __init__(self):
        self.srmode = False
        self.bbmode = False

        self.offset = 0
        self.interval = 0
        self.wrapperName = ""
        self.hiddenName = ""
        self.hidden = []
        self.wrapper = []
        self.handleArgs()

        



    def handleArgs(self): 
        # FLAGS = {"-s":False, "-r":False,  "-b":False,  "-B":False,  "-o":0, "-i":0, "-w":"",  "-h":""}
        commandArgs = sys.argv
        
        # assure the flags are correct

        # check to see if the system has no -s or -r flags
        if not ("-s" in commandArgs or "-r" in commandArgs):
            print("NEED TO SPECIFY WHETHER YOU ARE STORING OR RETRIEVING [-s,-r]")
            raise SyntaxError
        
        # check to see if the system has no too many -s and -r flags
        if ("-s" in commandArgs and "-r" in commandArgs):
            print("CANNOT STORE AND RETRIEVE")
            raise SyntaxError

        if not ("-b" in commandArgs or "-B" in commandArgs):
            print("NEED TO SPECIFY THE MODE: BIT [-b] or BYTE [-B]")
            raise SyntaxError
        
        if ("-b" in commandArgs and "-B" in commandArgs):
            print("CANNOT BIT AND BYTE")
            raise SyntaxError
        
        for val in commandArgs:
            # the mandatory arguments
            if val[1] == "s" or val[1] == "R":
                self.srmode = True if val[1] == "s" else False
            if val[1] == "b" or val[1] == "B":
                self.srmode = True if val[1] == "b" else False
            
            if val[1] == "o":
                self.offset = int(val[2:])
            
            if val[1] == "i":
                self.interval = int(val[2:])
            
            if val[1] == "w":
                # self.wrapper = val[2:]
                self.wrapper = loadfiles(val[2:])
                self.wrapperName = val[2:]

            if val[1] == "h":
                # self.hidden = val[2:]
                self.hidden = loadfiles(val[2:])
                self.hiddenName = val[2:]

        
    
    def __str__(self):
        out = "\n"
        out += "OFFSET:\t\t{}\n".format(self.offset)
        out += "INTERVAL:\t{}\n".format(self.interval) if self.interval != 0 else ""
        out += "WRAPPER:\t{}\n".format(self.wrapperName) if len(self.wrapperName) != 0 else ""
        out += "HIDDEN:\t\t{}\n".format(self.hiddenName) if len(self.hiddenName) != 0 else ""
        return out

    def process(self):
        
        # checks for bit mode
        if not self.bbmode:
            # INTERVAL = floor((len(self.wrapperName) - self.offset) / (len(self.hidden) + len(SENTINEL)) )
            self.interval = INTERVAL if self.interval == 0 else self.interval

            # store mode
            if self.srmode:

                i = 0
                # the offset, which changes
                poker = self.offset
                while (i < len(self.hidden)):
                    self.wrapper[poker]
                    poker += self.interval
                    i   += 1
            
                i = 0
                while (i < SENTINEL):
                    self.wrapper[poker] = SENTINEL[i]
                    poker += 1
                    i += 1

            # EXTRACTION
            else:
                poker = self.offset
                output = []
                thestopcounter = 0
                while (poker < len(self.wrapper)):
                    b = self.wrapper[poker]  
                    if (b in SENTINEL):
                        print(b)     
                    if(b in SENTINEL and thestopcounter == 0):
                        thestopcounter += 1
                    elif (b == SENTINEL[thestopcounter] and thestopcounter > 0):
                        thestopcounter += 1
                        if thestopcounter >= len(SENTINEL)-1:
                            sys.stdout.buffer.write(bytearray(output))
                            return
                            # pass
                    else:
                        thestopcounter = 0
                    
                    output.append(b)
                    poker += self.interval
                
                sys.stdout.buffer.write(bytearray(output))
                

        # otherwise do the byte mode
        else:
            pass



test = Steg()
test.process()

# print(test)

# test = [0,255,0,255,0]
# print(checkSentinel(True,test))



""" 
IF WE WERE ADULTS AND NOT KIDS WHO WANTED TO CREATE GARBAGE CODE
"""
# # start the parser
# my_parser = argparse.ArgumentParser(description='Use steganography with files')
# # Add the arguments
# my_parser.add_argument('-s',metavar='store',type=bool,help='store mode', default=False, nargs="?")
# my_parser.add_argument('-r',metavar='retrieve',type=bool,help='retrieve mode', default=False,nargs="?")

# my_parser.add_argument('-b',metavar='bit',type=bool,help='bit-mode', default=False,nargs="?")
# my_parser.add_argument('-B',metavar='byte',type=bool,help='byte-mode', default=False,nargs="?")


# my_parser.add_argument('-o',metavar='offset',type=int,help='bit-mode')
# my_parser.add_argument('-i',metavar='interval',type=int,help='byte-mode')
# my_parser.add_argument('-w',metavar='wrapper',type=str,help='bit-mode')
# my_parser.add_argument('-h',metavar='hidden',type=str,help='byte-mode')




# args = my_parser.parse_args()