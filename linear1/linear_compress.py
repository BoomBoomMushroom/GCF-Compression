from decimal import Decimal, getcontext
import struct
import sys

# Some dummy placeholder data right now
data = "01010101011101101001010011101000"

# Stack overflow | https://stackoverflow.com/questions/16444726/binary-representation-of-float-in-python-bits-not-hex
def floatToBinary(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))

# ChatGTP from stack overflow function above
def binaryToFloat(binary):
    int_representation = int(binary, 2)
    byte_representation = int_representation.to_bytes(4, byteorder='big')
    return struct.unpack('!f', byte_representation)[0]

def reconstructFloatFromBinary(binary):
    valRemade = binaryToFloat(binary)
    # I'm seeing a trend of `-2.315328174518072e-06` in error
    #valRemade -= 1.7595162882244608e-08
    return valRemade

"""
val = 0.566643518495688
print(val)

binVal = floatToBinary(val)
print(binVal)

valRemade = reconstructFloatFromBinary(binVal)

print(valRemade)
print(valRemade - val)

sys.exit()
"""

def calcSlope(x1, y1, x2, y2):
    return (x2 - x1) / (y1 - y2)

def intToBin(value):
    return bin(value).split("0b")[1]

def multiplyLargeIntByFloat(largeInt, floatNum):
    getcontext().prec = 1_000_000_000_000 # 1 Trillion digits
    
    largeIntDecimal = Decimal(largeInt)
    floatDecimal = Decimal(floatNum)
    
    result = largeIntDecimal * floatDecimal
    
    return result
    


dataFile = "linear_compress.py"
#dataFile = "data.txt"
outData = bytes()
with open(dataFile, "rb") as f:
    data = f.read()
    dataLen = len(data)
    
    dataBinary = intToBin(int.from_bytes(data))
    dataLenBinary = len(dataBinary)
    
    dataMiddle = dataLen // 2
    part1 = data[:dataMiddle]
    part2 = data[dataMiddle:]
    
    part1Int = int.from_bytes(part1)
    part2Int = int.from_bytes(part2)
    
    slope = part2Int / part1Int
    
    slopeStr = str(slope) + "."
    
    # Write output to string
    slopeBytes = (slopeStr).encode()
    outData = b''.join([slopeBytes, part1])
    # Done

    slopeBinSplits = slopeStr.split(".")
    slopeFromBinary = float(slopeBinSplits[0] + "." + slopeBinSplits[1])
    
    outPt2 = part1Int * Decimal(str(slopeFromBinary))
    
    #print(part2Int)
    
    print(part2Int - outPt2)
    
    #print(slope, "*", part1Int, "=", part2Int)
    

with open("out.txt", "wb") as f:
    f.write(outData)

