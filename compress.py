import sympy
from fractions import Fraction
import math

# Some dummy placeholder data right now
data = "01010101011101101001010011101000"

dataFile = "compress.py"
#data = "".join(f"{n:08b}" for n in open(dataFile, "rb").read())

# tack geeksforgeeks! https://www.geeksforgeeks.org/python-split-string-in-groups-of-n-consecutive-characters/#
def splitStrEveryNCharacters(string, n=10):
    return [(string[i:i+n]) for i in range(0, len(string), n)]

def intToTwosComplementBinary(n):
    bit_length = 0
    if n >= 0:
        # For non-negative numbers, the bit length is just the length of the binary representation
        bit_length = n.bit_length() + 1  # +1 for the sign bit
    else:
        # For negative numbers, calculate the minimum bits needed in two's complement
        bit_length = int(math.log2(abs(n))) + 2  # +1 for the sign, +1 for the two's complement
    
    if n >= 0:
        # For positive numbers, just return the binary representation with the specified bit length
        bin_repr = format(n, f'0{bit_length}b')
    else:
        # For negative numbers, get the two's complement
        bin_repr = format((1 << bit_length) + n, f'0{bit_length}b')
    return bin_repr

def twosComplementBinToInt(bStr):
    bit_length = len(bStr)
    
    # Check if the number is negative
    if bStr[0] == '1':
        # Invert the bits and add 1 to get the magnitude
        int_value = -((1 << bit_length) - int(bStr, 2))
    else:
        # If the number is positive, simply convert the binary string to an integer
        int_value = int(bStr, 2)
    
    return int_value

def splitData(data):
    # determine split algorithm
    # ex. every nibble, every byte, each bit?
    # 1/2 of the data, 1/3?
    
    # We'll just pass the binary as a string for now
    
    dataLength = len(data)
    
    #out = splitStrEveryNCharacters(data, 1) # Every Bit
    #out = splitStrEveryNCharacters(data, 4) # Every Nibble
    out = splitStrEveryNCharacters(data, round(dataLength/2)) # 1/2 of the string
    #out = splitStrEveryNCharacters(data, round(dataLength/3)) # 1/3 of the string
    #out = splitStrEveryNCharacters(data, round(dataLength/4)) # 1/4 of the string
    #out = splitStrEveryNCharacters(data, round(dataLength/16)) # 1/16 of the string
    #out = splitStrEveryNCharacters(data, 80)
    
    
    
    return out

def convertDataArrayIntoPoints(dataArray):
    out = []
    
    for i in range(len(dataArray)):
        dataBinary = dataArray[i]
        valueOfData = int(dataBinary, 2)
        point = (1 * i, valueOfData)
        out.append(point)
        #print(dataBinary, valueOfData, point)
    
    return out

def pointsToPolynomialCoefficients(points):
    coefficients = []
    
    matrix = []
    degree = len(points) - 1
    
    # ax^3 + bx^2 + cx + d = y
    for point in points:
        matrix.append([])
        
        x = point[0]
        y = point[1]
        for n in range(degree, -1, -1):
            xOfDegree = x ** n
            matrix[-1].append(xOfDegree)
        
        matrix[-1].append(y)
    
    matrix = sympy.Matrix(matrix)
    #print(matrix)
    
    matrix_rref = matrix.rref()
    #print(matrix_rref)
    
    for i in range(matrix_rref[0].rows):
        matrixValue = matrix_rref[0].row(i)[-1]
        coefficients.append(matrixValue)
    
    # Y multiplier
    coefficients.append(1)
    coefficients = coefficients[::-1]
    
    print("Raw Coefficients: ", coefficients)
    
    for i in range(len(coefficients)):
        coefficients[i] = eval(str(coefficients[i]))
    
    return coefficients

def polynomialCoefficientsToEquation(coefficients):
    out = str(coefficients[0]) + "y = "
    for i in range(1, len(coefficients)):
        coef = coefficients[i]
        n = i - 1
        
        if(n != 0): out += " + "
        
        out += str(coef)
        if(n == 0): continue
        
        out += "x"
        if(n > 1): out += "^" + str(n)
    return out

def coefficientsToInts(coefficients):
    multiplier = 1
    
    for value in coefficients:
        if round(value) == value: continue
        # Non-int found! Let's make it an int!
        fractional_part = value - int(value)
        fraction = Fraction(fractional_part).limit_denominator()
        multiplier = fraction.denominator
        
    # No changes, let them know that
    if multiplier == 1:
        # Get a nice number w/o the .0 at the end
        for i in range(len(coefficients)):
            coefficients[i] = int(coefficients[i])
        
        return coefficients, False
    
    for i in range(len(coefficients)):
        coefficients[i] *= multiplier
    
    return coefficients, True

dataArr = splitData(data)
#print(dataArr)

points = convertDataArrayIntoPoints(dataArr)

print(points)

coefficients = pointsToPolynomialCoefficients(points)

# Make coefficients into ints 
while True:
    coefficients, needToLoopAgain = coefficientsToInts(coefficients)
    if needToLoopAgain: continue
    break

def reduceCoefficients(coefficients):
    coefficients = coefficients[1:]
    
    gcd = math.gcd(*coefficients)
    for coeff in coefficients[2:]:
        gcd = math.gcd(gcd, coeff)
    
    reducedCoefficients = [c // gcd for c in coefficients]
    
    return reducedCoefficients, gcd

reducedCoefficients, gcd = reduceCoefficients(coefficients)
print(reducedCoefficients, gcd)
#coefficients = [gcd] + reducedCoefficients

print(coefficients)

polyEquation = polynomialCoefficientsToEquation(coefficients)
print(polyEquation)

outData = ""
outData += bin(coefficients[0]).split("0b")[1]
for i in range(1, len(coefficients)):
    c = coefficients[i]
    twosBinary = intToTwosComplementBinary(c)
    outData += twosBinary

with open("outData.txt", "w") as f:
    f.write(polyEquation)

print(outData, len(outData))
print(len(data))