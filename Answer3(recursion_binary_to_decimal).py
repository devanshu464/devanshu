'''num = int(input("enter the number entered by user\t"))

while num > 0:   
    remainder = num % 2
    print(remainder, end = " ")
    quotient = num // 2
    #print(quotient)
#print(num)
    num = quotient'''
    
'''decimal to binary using recursion'''

def decimalToBinary(num):
    
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end=' ')


# decimal number
number = int(input("Enter any decimal number: "))

decimalToBinary(number)