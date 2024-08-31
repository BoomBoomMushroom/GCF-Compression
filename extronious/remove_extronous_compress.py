import math

def calcNumberMaxTimesCharacterAppearsInStringInRow(string, char):
    result = 0
    count = 0
    for c in string:
        if c == char:
            count += 1
            continue
        
        result = max(result, count)
        count = 0
    
    return result

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

dataFile = "./remove_extronious_compress.py"
with open(dataFile, "rb") as f:
    byte = f.read()
    dataStr = binaryOfInt(int(byte.hex(), 16))

"""
splitEveryX = 1024
dataArr = splitStringEveryNChar(dataStr, splitEveryX)

print("Data Arr: ", dataArr)

# turn data into ints
intArr = []
for data in dataArr:
    intArr.append(int(data, 2))

print("Int Arr: ", intArr)
"""

"""
outNoEOF = ""
for value in intArr: outNoEOF += binaryOfInt(value)

zeroStreakInData = calcNumberMaxTimesCharacterAppearsInStringInRow(outNoEOF, "0")
eof = "0" * zeroStreakInData
eofSizeBytePrefix = binaryOfInt(zeroStreakInData).zfill(8)

outData = eofSizeBytePrefix + binaryOfInt(splitEveryX).zfill(8)
for value in intArr:
    binaryString = binaryOfInt(value)

    if len(binaryString) < splitEveryX:
        outData += eof
    outData += binaryString
"""

outData = binaryOfInt( len(dataStr) )
outData += binaryOfInt( int(dataStr,2) )


print(len(dataStr))
print(len(outData))
#print(outData)

#print(zeroStreakInData)