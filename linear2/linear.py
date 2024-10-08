import precise_division

import sys
from fractions import Fraction

def write_part(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)

def read_part(filename):
    with open(filename, 'rb') as f:
        return f.read()

def save_quotient(filename, quotient):
    with open(filename, 'w') as f:
        f.write(str(quotient))

def load_quotient(filename):
    with open(filename, 'r') as f:
        data = float(f.read())
        return data

def compress(part_a_file, part_b_file, quotient_file):
    part_a = read_part(part_a_file)
    part_b = read_part(part_b_file)
    
    # Convert binary data to integers
    a = int.from_bytes(part_a, byteorder='big')
    b = int.from_bytes(part_b, byteorder='big')
    
    if a == 0:
        raise ZeroDivisionError("Part A cannot be zero for division.")
    
    # Calculate quotient B / A
    #quotient = b / a
    
    # use my precise division algorithm
    quotient = precise_division.divide(b, a)
    
    print(b, "\n\n")
    
    save_quotient(quotient_file, quotient)
    
    # Save Part A to a file
    write_part(part_a_file, part_a)

def decompress(part_a_file, quotient_file, recovered_b_file):
    part_a = read_part(part_a_file)
    quotient = load_quotient(quotient_file)
    
    # Convert binary data to integers
    a = int.from_bytes(part_a, byteorder='big')
    
    # Recover B
    #b = a * quotient
    
    # use my precise division algorithm's multiply
    b = precise_division.multiply(a, quotient)
    
    print(b)
    
    b = int(b)
    write_part(recovered_b_file, b.to_bytes((b.bit_length() + 7) // 8, byteorder='big'))

def fileIntoParts(dataFile, part_a_file, part_b_file):
    with open(dataFile, "rb") as f:
        data = f.read()
        dataLen = len(data)
        
        dataMiddle = dataLen // 2
        part1 = data[:dataMiddle]
        part2 = data[dataMiddle:]
        
        part1Int = int.from_bytes(part1)
        part2Int = int.from_bytes(part2)
        write_part(part_a_file, part1Int.to_bytes((part1Int.bit_length() + 7) // 8, byteorder='big'))
        write_part(part_b_file, part2Int.to_bytes((part2Int.bit_length() + 7) // 8, byteorder='big'))

# Example usage
src_file = './linear2/linear.py'
part_a_file = './linear2/part_a.bin'
part_b_file = './linear2/part_b.bin'
quotient_file = './linear2/quotient.bin'
recovered_b_file = './linear2/recovered_b.bin'


fileIntoParts(src_file, part_a_file, part_b_file)

# Compress
compress(part_a_file, part_b_file, quotient_file)

# Decompress
decompress(part_a_file, quotient_file, recovered_b_file)
