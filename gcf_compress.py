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

dataFile = "./gcf_compress.py"
with open(dataFile, "rb") as f:
    byte = f.read()
    dataStr = binaryOfInt(int(byte.hex(), 16))

splitEveryX = 1024
dataArr = splitStringEveryNChar(dataStr, splitEveryX)

print("Data Arr: ", dataArr)

# turn data into ints
intArr = []
for data in dataArr:
    intArr.append(int(data, 2))

print("Int Arr: ", intArr)


dataPatches = 2
intPatches = []
for i in range(len(intArr)):
    if i % dataPatches == 0: intPatches.append([])

    value = intArr[i]
    intPatches[-1].append(value)

print("Int Patches: ", intPatches)

zeroStreakInData = calcNumberMaxTimesCharacterAppearsInStringInRow(dataStr, "0")
eof = "0" * zeroStreakInData
outData = binaryOfInt(dataPatches)

print("EOF, EOF.len: ", eof, len(eof))

for patch in intPatches:
    gcd = math.gcd(*patch)
    newPatch = [x // gcd for x in patch]

    for value in newPatch:
        outData += eof
        outData += binaryOfInt(value)

    print("Old Patch, New Patch, GCD: ", patch, newPatch, gcd)


print(len(dataStr))
print() # Buffer between the two
print(len(outData))

with open('./out.txt', 'wb') as f:
    queue = ""
    for char in outData:
        queue += char
        if len(queue) >= 8:
            f.write(bytes(int(queue, 2)))
            queue = ""
    