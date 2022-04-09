"""Hexadecimal (or hex) is a base 16 system used to simplify how binary is represented.
A hex digit can be any of the following 16 digits: 0 1 2 3 4 5 6 7 8 9 A B C D E F.
Each hex digit reflects a 4-bit binary sequence."""


def decimal_to_hexadecimal(num):
    
    #empty list to contain the numbers
    result = []

    while num:
        remainder = num % 16
        num = num // 16
        if remainder < 10:
            result.append(remainder)
        else:
            result.append(chr(remainder+55))
    return result[::-1]


print(decimal_to_hexadecimal(500))
