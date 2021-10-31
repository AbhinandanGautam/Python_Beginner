operator = input('Enter operator : ')
op1 = int(input('Enter operand 1 : '))
op2 = int(input('Enter operand 2 : '))

if(operator == '+'):
    print("Result = ",op1+op2)
elif(operator == '-'):
    print("Result = ",op1-op2)
elif(operator == '*'):
    print("Result = ", op1*op2)
elif(operator == '/'):
    print("Result = ", op1/op2)
elif(operator =='**'):
    print("Result = ", op1**op2)
else:
    print("Enter correct data")