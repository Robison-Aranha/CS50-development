import math
number = input("Number: ")
counter = len(number)
soma1 = 0
soma2 = 0

print(counter)
number = int(number)
num1 = 0
verificação = 1
verificação2 = 0
verificação3 = 0
for i in range(0, counter - 2):
    verificação = verificação * 10
    num1 = number / verificação
num1 = int(num1)
verificação = 100
verificação2 = 10
soma2 += int(number % (verificação / 10))
for c in range(0, int(counter / 2)):
    verificação3 = int((number % verificação) / verificação2) * 2
    soma1 += int((verificação3 % 10) + ((verificação3 % 100) / 10))
    soma2 += int((number % (verificação * 10)) / (verificação2 * 10))
    verificação2 = int(verificação2 * 100)
    verificação = int(verificação * 100)
soma2 = int(soma1 + soma2) 
print(soma2)
if soma2 % 10 == 0:
    if counter == 15:
        if num1 == 34 or num1 == 37:
            print("AMEX\n")
        else:
            print("INVALID\n")
            
    elif counter == 16 or counter == 13:
        print((num1 % 100) / 10)
        if int((num1 % 100) / 10) == 4:
            print("VISA\n")
            
        elif num1 == 51 or num1 == 52 or num1 == 53 or num1 == 54 or num1 == 55:
            print("MASTERCARD\n")
            
        else:
            print("INVALID\n")
            
    else:
        print("INVALID\n")
        
else:
    print("INVALID\n")
