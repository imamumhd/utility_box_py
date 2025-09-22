from text_utils import count_words, reverse_words, make_uppercase
from math_utils import add, subtract, multiply, divide  
from file_utils import read_file, save_to_file

choice = input("what do you want to do? (text, math, file): ").lower()

if choice == "text" :
  operation =input("which operation? (count, reverse, uppercase): ").lower()
  text = str(input("Enter text: "))
  if operation == "count" :
    print(count_words(text))
  elif operation == "reverse" :
    print(reverse_words(text))
  elif operation =="uppercase" :
    print(make_uppercase(text))
  else :
    print('\nInvalid Input!')
    
elif choice == "math" :
  operation =input("which operation? (add, subtract, multiply, divide): ").lower()
  num1 = float(input("Enter num1: "))
  num2 = float(input("Enter num2: "))
  if operation == "add" :
    print(num1+num2)
  elif operation == "subtract" :
    print(num1-num2)
  elif operation =="multiply" :
    print(num1*num2)
  elif operation =="divide" :
    print(num1/num2)
  else :
    print('\nInvalid Input!')

elif choice == "file":
    operation = input("Which operation? (save, read): ").lower()
    filename = input("Enter filename: ")

    if operation == "save":
        text = input("Enter text to save: ")
        save_to_file(filename, text)
    elif operation == "read":
        read_file(filename)   
    else:
        print('\nInvalid Input!')


