decimal = input("Enter a decimal number: ")


def DecimalToBinary(decimal):       
    if decimal > 1: 
        DecimalToBinary(decimal // 2) 
    print(decimal % 2, end = '')


# Calling the function
DecimalToBinary(int(decimal))