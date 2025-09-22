def count_words(text):
    text = text.lower()
    words = text.split()
    return len(words)

def reverse_words(text):
    words = text.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

def make_uppercase(text):
    text = text.upper()
    return text

while True:
    print('\n1. Count Words')
    print('2. Reverse Words')
    print('3. Make Uppercase')
    print('4. Exit')
    choice = input('Enter from the above options: ')
    if choice == '1':
        text = input('Enter the text you want to count: ')
        print(count_words(text))
    elif choice == '2':
        text = input('Enter the text you want to reverse: ')
        print(reverse_words(text))
    elif choice == '3':
        text = input('Enter the text you want to make uppercase: ')
        print(make_uppercase(text))
    elif choice == '4':
        break
    else:
        print('\nInvalid Input!')
