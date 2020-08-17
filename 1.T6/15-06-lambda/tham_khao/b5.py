binary_string = input("Enter a binary number :")

try:
    decimal = int(binary_string,2)  
    print("The decimal value is :", decimal)    
    
except ValueError:
    print("Invalid binary number")