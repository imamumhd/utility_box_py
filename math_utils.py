while True:
    num1 = int(input("Enter num1: "))
    operato = input("Enter operato(+,-,/,*):")
    num2 = int(input("Enter num2: "))

    if operato == "+":
        
        print(num1+num2)
        
    elif operato == "-":
        result = num1-num2
        print(result)
                
    elif operato == "/":
        if num2 == 0:
         print("can't divide by zero")
        else:    
         result = num1/num2
         print(result)
                
    elif operato == "*":
        result = num1*num2
        print(result)
                
else:
        print("invalid entry")
