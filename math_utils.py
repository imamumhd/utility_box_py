
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "can't divide by zero"
    return a / b


while True:
    print('\n1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Exit')
    choice = input('Enter from the above options: ')
    if choice in ['1', '2', '3', '4']:
        num1 = float(input('Enter num1: '))
        num2 = float(input('Enter num2: '))
        if choice == '1':
            print(add(num1, num2))
        elif choice == '2':
            print(subtract(num1, num2))
        elif choice == '3':
            print(multiply(num1, num2))
        elif choice == '4':
            print(divide(num1, num2))
    elif choice == '5':
        break
    else:
        print('\nInvalid Input!')
    
