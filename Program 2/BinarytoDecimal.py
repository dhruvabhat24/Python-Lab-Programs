def binary_to_decimal(binary):
    decimal=0
    for digit in binary:
        decimal= decimal*2+int(digit)
        return decimal
def octal_to_hexadecimal(octal):
    decimal=0
    for digit in octal:
        decimal =decimal*8+int(digit)
        hexadecimal=hex(decimal).lstrip("ox").upper
        return hexadecimal
    num=input("Enter a binary or octal number:")
    if set(num).issubset({"0","1"}):
        decimal=binary_to_decimal(num)
        print(num,"in decimal is:",decimal)
    elif set(num).issubset({"0","1","2","3","4","5","6","7"}):
        hexadecimal=octal_to_hexadecimal(num)
        print(num,"in hexadecimal is:",hexadecimal)
    else:
        print("Error:The input number must be binary or octal")