op_type = input ("choose an operation to use :")

a = int(input("enter first number :"))
b = int(input("enter second number :"))

run = True

def add(a, b):
    print( a + b) 

def sub(a, b):
    print( a - b) 

def multiply(a, b):
    print( a * b)

def divide(a, b):
    print( a / b)

while run :
    
    if "+" in op_type:
        add(a , b)
        break
    if "-" in op_type:
        sub(a , b)
        break
    if "*" in op_type:
        multiply(a , b)
        break
    if "/" in op_type:
        divide(a , b)
        break




