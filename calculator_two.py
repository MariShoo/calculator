#  iphone calulator imitation 

import math 

op_type = input("Choose an operation to use (+, -, *, /, ^, root): ")

if op_type in ["+", "*"]:
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]      
else :
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    
run = True

def add(a, b):
    print( a + b) 

def sub(a, b):
    print( a - b) 

def multiply(numbers):
    print(math.prod(numbers))

def divide(a, b):
      print( a / b)

def sqrt(a):
    print(math.sqrt(a))

def power(a, b):
    print(math.pow(a, b))

while run :
    
    if "+" in op_type:
            add(a , b)
            break
    elif "-" in op_type:
            sub(a , b)
            break
    elif "*" in op_type:
         multiply(numbers)
         break
    elif "/" in op_type:
             if b == 0:
                print("Error: Division by zero!")
                break
             else:
                divide(a / b)
                break
    elif "^" in op_type:
            print(math.pow(a , b ))
            break
    if "root" in op_type:
            print(math.sqrt(a))
            break

