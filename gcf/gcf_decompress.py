import math

def getEOFLengthFromString(string, char):
    outs = []
    count = 0
    for c in string:
        if c == char:
            count += 1
            continue
        
        outs.append(count)
        count = 0
    
    outs = list(filter((0).__ne__, outs))
    #print(outs)

    return max(set(outs), key = outs.count)

def splitStringEveryNChar(string, n):
    dataArr = []
    for i in range(len(string)):
        if i % n == 0: dataArr.append("")

        char = string[i]
        dataArr[-1] += char
    return dataArr

def binaryOfInt(value):
    return bin(value).split("0b")[1]


dataStr = "01011010101011101101011010101001"

eofSize = 0

dataFile = "./out.txt"
with open(dataFile, "rb") as f:
    eofbyte = f.read(1)
    print(eofbyte.hex(), eofbyte)
    eofSize = int(eofbyte.hex(), 16)

    byte = f.read()
    dataStr = binaryOfInt(int(byte.hex(), 16))

eofLen = getEOFLengthFromString(dataStr, "0")

print(eofSize)
