from decimal import Decimal, getcontext

def multiplyLargeIntByFloat(largeInt, floatNum):
    getcontext().prec = 1_000_000_000_000 # 1 Trillion digits
    
    largeIntDecimal = Decimal(largeInt)
    floatDecimal = Decimal(floatNum)
    
    result = largeIntDecimal * floatDecimal
    
    return result

outBytes = b''

with open("out.txt", "rb") as f:
    data = f.read()
    dataStrAscii = data.decode("ascii")
    
    dotSplits = dataStrAscii.split(".")
    slopeString = dotSplits[0] + "." + dotSplits[1]
    slope = float(slopeString)
    
    # Data Format
    # int.decimal.DATA
    restOfData = data[len(slopeString)+1:]
    
    part1 = int.from_bytes(restOfData)
    
    # slope = part2 / part1
    # slope * part1 = part2
    part2 = multiplyLargeIntByFloat(part1, slope)
    part2 = int(part2)
    
    print(part2)
    
    numBytes = (part2.bit_length() + 7) // 8
    uncompressed = part2.to_bytes(numBytes, byteorder='big')    
    
    outBytes = restOfData + uncompressed

with open("unout.txt", "wb") as f:
    f.write(outBytes)