from datetime import datetime

EPOCH="2017 01 01 00 00 00" 
REF = ["YYYY","MM","DD","HH","MM","SS"]

def timePassed(start,stop):
    
    if (len(start) != len(stop)):
        print('the sizes of time are different')
        return -1

    # flip them around
    start,stop = start[::-1],stop[::-1]


    carry = 0
    delta = []
    counter = len(REF)
    # ep = epoch, cur = current
    for ep,cur in (zip(start.split(" "),stop.split(" "))):
        # again
        ep,cur = ep[::-1],cur[::-1]
        # convert to int
        epint,curint = int(ep),int(cur)
        print("EPOCH: {}\tCURRENT: {}".format(ep,cur))
        if epint < curint:
            if REF[counter] in ["HH","MM","SS"]:        
                carry = 1
                epint += 60
                delta[counter] = str(epint-curint)
            
            if REF[counter] == "DD":        
                carry = 1
                epint += 7

            if REF[counter] == "MM":        
                pass
            
            if REF[counter] == "YYYY":        
                pass
        
        else:
            pass


        counter -= 1

now = datetime.now()

current_time = now.strftime("%Y %m %d %H %M %S")
# print("Current Time =", current_time)

print(timePassed(EPOCH, current_time))