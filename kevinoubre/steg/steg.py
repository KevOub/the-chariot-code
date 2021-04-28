
import os
import sys
from math import floor

# CURRENLTY IN LEFT TO RIGHT STORAGE MODE
SENTINEL = [0x0,0xff,0x0,0x0,0xff,0x0]


""" 
python Steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]
"""

def loadfiles(file):
    with open(file, "rb") as f:
        return f.read()

# def checkSentinel(mode,arr):
#     # mode:True = right to left 
#     if mode:
#         if len(arr) != len(SENTINEL):
#             return False
#         g2g = [True if val == arr[count] else False for count,val in enumerate(SENTINEL)]
#         return all(g2g)
            
    
#     # left to right
#     else:
#         pass


class Steg():
    """ 
    s/r mode is either store or retrieve: True is store, False is retrieve
    b/B mode is either bit or Byte: True is bit, False is Byte
    """
    def __init__(self):
        self.srmode = False
        self.bbmode = False

        # self.reverse = False

        self.offset = 0
        self.interval = 0
        self.wrapperName = ""
        self.hiddenName = ""
        self.hidden = []
        self.wrapper = []
        self.handleArgs()

        
    def reachedSentinel(self,poker):
        # goes through [start,stop,step] and see if it matches the sentinel
        try:
            return [self.wrapper[i] for i in range(poker,poker + (self.interval * 6), self.interval)] == SENTINEL
        except:
            return -1




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
                self.bbmode = True if val[1] == "b" else False
            
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

    def retrieveByteMode(self):
        poker = self.offset
        output = []
        thestopcounter = 0
        while (poker < len(self.wrapper)):
            b = self.wrapper[poker]  
             
            if b == SENTINEL[0]:

                finished = self.reachedSentinel(poker)
                if finished == -1:
                    return

                if finished:
                    sys.stdout.buffer.write(bytearray(output))
                    return
            

            """ 
            if b == SENTINEL[thestopcounter]:
                thestopcounter += 1
            else:
                thestopcounter = 0
            
            if thestopcounter >= len(SENTINEL):
                sys.stdout.buffer.write(bytearray(output))
                return
             """
            poker += self.interval
            output.append(b)

    def retrieveBitMode(self):
        out = []
        poker = self.offset
        thestopcounter = 0
        while poker < len(self.wrapper):
            b = 0
            for i in range(0,8):
                try:
                    b |= (self.wrapper[poker] & 0x0000001)
                except:
                    return 

                if i < 7:        
                    b = (b << 1) & (2 ** 8 - 1)
                    # print(("{0:b}".format(b)))

                    poker += self.interval

            


            if b == SENTINEL[thestopcounter]:
                thestopcounter += 1
            else:
                thestopcounter = 0
            

            if thestopcounter >= len(SENTINEL):
                sys.stdout.buffer.write(bytearray(out))
                return

            poker += self.interval
            out.append(b)




    def process(self):
        
        # checks for bit mode
        if not self.bbmode:
            # STORE
            if self.srmode:
                i = 0
                # the offset, which changes
                poker = self.offset
                while (i < len(self.hidden)):
                    self.wrapper[poker]
                    poker += self.interval
                    i += 1
            
                i = 0
                while (i < len(SENTINEL) ):
                    self.wrapper[poker] = SENTINEL[i]
                    poker += 1
                    i += 1

            # RETRIEVE
            else:
                self.retrieveByteMode()

            # else:
            #     poker = self.offset
            #     output = []
            #     thestopcounter = 0
            #     while (poker < len(self.wrapper)):
            #         b = self.wrapper[poker]  

            #         if b in SENTINEL:

            #             finished = self.reachedSentinel(poker)
            #             if finished == -1:
            #                 return

            #             if finished:
            #                 sys.stdout.buffer.write(bytearray(output))
            #                 return
                    
            #         poker += self.interval
            #         output.append(b)

                
                # sys.stdout.buffer.write(bytearray(output))
                

        # otherwise do the byte mode
        if self.bbmode:
                
            # STORE
            if self.srmode:
                pass

            # RETRIEVE
            else:

                self.retrieveBitMode()
                # INTERVAL = floor((len(self.wrapperName) - self.offset) / (len(self.hidden) + len(SENTINEL)) )
                # INTERVAL = 1
                # self.interval = INTERVAL if self.interval == 0 else self.interval

                    # print("---")
                    # print("PRE {}".format(b))
                    # b = int('{0:b}'.format(b)[::-1], 2)
                    # print(("{0:b}".format(b)))
                    # print("POST {}".format(b))

                    # print(b)
""" 
                out = []
                poker = self.offset
                thestopcounter = 0
                while poker < len(self.wrapper):
                    b = 0
                    for i in range(0,8):
                        try:
                            b |= (self.wrapper[poker] & 0x0000001)
                        except:
                            return 

                        if i < 7:        
                            b = (b << 1) & (2 ** 8 - 1)
                            # print(("{0:b}".format(b)))

                            poker += self.interval

                    


                    if b == SENTINEL[thestopcounter]:
                        thestopcounter += 1
                    else:
                        thestopcounter = 0
                    

                    if thestopcounter >= len(SENTINEL):
                        sys.stdout.buffer.write(bytearray(out))
                        return

                    poker += self.interval
                    out.append(b)
 """
                # return sys.stdout.buffer.write(bytearray(out))




test = Steg()
test.process()

# print(test)

# test = [0,255,0,255,0]
# print(checkSentinel(True,test))

