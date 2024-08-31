import math

# Based off of this Math Video (For Kids)
# https://www.youtube.com/watch?v=LZthuV3ZpCY
def divide(b, a, maxRepeatingPlaces=10) -> str:
    # b / a
    if b == 0: raise ZeroDivisionError
    
    #aStr = str(a)
    bStr = str(b)
    
    output = ""
    divideBuffer = 0
    
    #   _____
    # a ) b
    
    placeBrought = 0
    def bringDownNextPlace(number, buffer, place):
        """
        while buffer < a:
            digit = number[place]
            if digit == ".":
                place += 1
                continue
            
            newBufferStr = str(buffer) + digit
            buffer = int(newBufferStr)
            place += 1
        """
        
        while buffer < a:
            digit = number[place]
            if digit == ".":
                place += 1
                continue
            
            newBufferStr = str(buffer) + digit
            buffer = int(newBufferStr)
            place += 1
            break
        
        return buffer, place
    
    # First find our first divide buffer
    
    divideBuffer = int(bStr[0])
    placeBrought = 1
    #divideBuffer, placeBrought = bringDownNextPlace(bStr, divideBuffer, placeBrought)

    #print(divideBuffer)
    # Now we start division
    
    lastBringDown = False
    while divideBuffer != 0:
        #input()
        n = 0
        while a * n < divideBuffer:
            n += 1
        
        if a * n > divideBuffer:
            n -= 1 # overshot by 1
        
        #print(aStr, bStr, output)
        #print(divideBuffer, placeBrought)
        #print(output)
        
        if n == 0:
            digitsB = len(bStr)
            if lastBringDown: output += "0"
            
            if digitsB == placeBrought:
                if '.' not in bStr:
                    bStr += "."
                    output += "."
                    placeBrought += 1
                bStr += "0"
            
            divideBuffer, placeBrought = bringDownNextPlace(bStr, divideBuffer, placeBrought)
            lastBringDown = True
            continue

        lastBringDown = False
        valToSub = a * n
        divideBuffer -= valToSub
        output += str(n)
        
        if '.' in output:
            # check for repeating decimal places
            decimals = output.split('.')[1]
            decimalCount = len(decimals)
            if decimalCount > 1_000_000:
                break
                print(f"100+ Decimals! {decimalCount}")
            
            if decimalCount < maxRepeatingPlaces: pass
            else:
                lastCharacters = decimals[-maxRepeatingPlaces:] # last characters of string
                repeatedCharacters = lastCharacters[-1] * maxRepeatingPlaces
                if lastCharacters == repeatedCharacters:
                    break
                
    output = output.strip("0")
    #print(type(output))
    #print(output, divideBuffer)
    return output

# This math video: https://www.youtube.com/watch?v=6AB39rtr6qc
# DOES NOT WORK
"""
def multiply(a, b):
    a = str(a)
    b = str(b)
    
    
    # get total decimal places
    decimalPlacesA = 0
    if '.' in a: decimalPlacesA = len(a.split(".")[1])
    
    decimalPlacesB = 0
    if '.' in b: decimalPlacesB = len(b.split(".")[1])
    
    totalDecimalPlaces = decimalPlacesA + decimalPlacesB
    
    prefix = "" # add a zero after each row of multiplying
    out = ""
    outs = []
    carry = 0
    
    #    a
    # x  b
    # ------
    
    for i in range(0, len(b)):
        out += prefix
        
        digitB = b[-i - 1]
        if(digitB == "."): continue
        digitB = int(digitB)
        #print(digitB)
        
        for j in range(0, len(a)):
            digitA = a[-j - 1]
            if(digitA == "."): continue
            digitA = int(digitA)
            
            multResult = digitB * digitA
            multResult += carry
            
            multStr = str(multResult)
            
            outAppend = multStr[-1] # the ones place
            out = outAppend + out

            carry = math.floor(multResult / 10)
            
            print(multResult, outAppend, carry)
        
        if carry != 0:
            out = str(carry) + out
        
        #print(f"{a}\n{b}\n---------------")
        #print(out)
        #print(totalDecimalPlaces)
        
        outs.append(out)
        prefix += "0"
    
    print(outs)
    print(totalDecimalPlaces)
    
    #print(a, b)
"""
# ChatGPT Code
def multiply(num1: str, num2: str) -> str:
    num1 = str(num1)
    num2 = str(num2)
    
    def remove_decimal(num: str) -> (str, int):
        if '.' in num:
            integer_part, decimal_part = num.split('.')
            return integer_part + decimal_part, len(decimal_part)
        else:
            return num, 0

    def add_strings(num1: str, num2: str) -> str:
        # Ensure num1 is the longer one
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0
        result = []
        
        for i in range(len(num1)):
            digit1 = int(num1[i])
            digit2 = int(num2[i]) if i < len(num2) else 0
            total = digit1 + digit2 + carry
            carry = total // 10
            result.append(total % 10)
        
        if carry:
            result.append(carry)
        
        return ''.join(map(str, result[::-1]))

    def multiply_strings(num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        num1 = num1[::-1]
        num2 = num2[::-1]
        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                mul = int(num1[i]) * int(num2[j])
                result[i + j] += mul
                if result[i + j] >= 10:
                    result[i + j + 1] += result[i + j] // 10
                    result[i + j] %= 10
        
        while result[-1] == 0:
            result.pop()
        
        return ''.join(map(str, result[::-1]))

    num1, decimal_places1 = remove_decimal(num1)
    num2, decimal_places2 = remove_decimal(num2)

    result = multiply_strings(num1, num2)

    decimal_places_total = decimal_places1 + decimal_places2
    if decimal_places_total == 0:
        return result

    if len(result) <= decimal_places_total:
        result = '0' * (decimal_places_total - len(result) + 1) + result

    result = result[:-decimal_places_total] + '.' + result[-decimal_places_total:]

    return result

if __name__ == "__main__":
    #divide(330, 8) # 8.3

    #fortyOneFiths = divide(41, 5) # 41.25
    #multiply(fortyOneFiths, 5) # 41

    #sevenSixths = divide(7, 6) # 1.166666 repeating
    #multiply(sevenSixths, 6.1) # should be 7?

    #oneHalf = divide(1, 2)
    #print(oneHalf)

    example = divide(182, 125)
    print(example)
    #multiply(example, 125)
    o = multiply(example, 125)
    o = o.split(".")[0]

    print(o)