# convert decimal to binary or octal or hexadecimal

class converter:
    @staticmethod
    def binary(num):
        arr = []
        while (num != 0):
            reminder = num % 2
            arr.append(reminder)
            num //= 2
        arr.reverse()
        return arr
    
    @staticmethod
    def octal(num):
        arr = []
        while (num != 0):
            reminder = num % 8
            arr.append(reminder)
            num //= 8
        arr.reverse()
        return arr
    
    @staticmethod
    def hexaDecimal(num):
        arr = []
        while(num != 0):
            reminder = num % 16
            if (reminder == 10 ):
                arr.append("A")
            elif (reminder == 11 ):
                arr.append("B")
            elif (reminder == 12 ):
                arr.append("C")
            elif (reminder == 13 ):
                arr.append("D")
            elif (reminder == 14 ):
                arr.append("E")
            elif (reminder == 15 ):
                arr.append("F")
            else:
                arr.append(reminder)
            num //= 16
        arr.reverse()
        return arr

num = int(input("Enter the number: "))
convert = converter()
result1 = convert.binary(num)
result2 = convert.octal(num)
result3 = convert.hexaDecimal(num)
print("Binary : ", result1)
print("Octal : ", result2)
print("HexaDecimal : ", result3)



# print(f"Decimal {num} to Binary {bin(num)[2:]}")
# print(f"Decimal {num} to Octal {oct(num)[2:]}")
# print(f"Decimal {num} to Hexadecimal {hex(num)[2:]}")