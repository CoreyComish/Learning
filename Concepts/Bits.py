# Purpose: Learn and explain what bits are in the context of programming

# What is a bit?
"""
A bit is the smallest unit of information on a computer
A bit can be 0 or 1
    Often time 0 maps to False, 1 maps to True
"""

# What is a byte?
"""
A byte is simply 8 bits
A kilobyte is 1000 bytes
A megabyte is 1,000,000 bytes or 1,000 kilobytes
A gigabyte is 1,000 megabytes
    and so on...
"""

# What is bit manipulation?
"""
Bit manipulation is the act of performing operations on bits
This can be useful for low-level device control, error detection algorithms, data compression, and more
"""

# Python Bitwise Operators
"""
    & = AND = Sets each bit to 1 if both bits are 1
    | = OR = Sets each bit to 1 if one of the two bits is 1
    ^ = XOR = Sets each bit to 1 if only one of two bits is 1
    ~ = NOT = Inverts all the bits
    << = Zero fill left shift = Shift left by pushing zeros in from the right and let the leftmost bits fall off
    >> = Signed right shift = Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

    0 & 0 = 0
    0 & 1 = 0
    1 & 1 = 1

    0 | 0 = 0
    0 | 1 = 1
    1 | 1 = 1

    0 ^ 0 = 0
    0 ^ 1 = 1
    1 ^ 1 = 0
"""

# What is Two's Complement?
"""
Imagine we're in a land of 8-bit integers...
We use the first bit to represent whether the integer is negative or not

    18 = 00010010
   -18 = 11101110

   (notice how each bit is inversed)

This is called the Two's complement
    1) Convert number to binary
    2) Invert bits
    3) Add 1
"""

# Examples

# Convert a bit string to it's base 2 int value
def printInt(bitString):
    print(int(bitString, base=2))

# Convert a bit string to it's hex value
def printHex(bitString):
    print("0x%x" % int(bitString, base=2))

# Convert a bit string to it's char value
def printChar(bitString):
    print(chr(int(bitString, base=2)))

def main():
    printInt('0010100')
    printHex('0010100')
    printChar('0010100')

if __name__ == "__main__":
    main()