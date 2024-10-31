 # Винятки

while True:
    try:
        number1 = ''
        number2 = ''
        while not number1.isdigit():
            number1 = input('Enter a number1: ')
        number1 = int(number1)
        command = str(input('Enter a command: '))
        while not number2.isdigit():
            number2 = input('Enter a number2: ')
        number2 = int(number2)
        if command == '+':
            print(number1 + number2)
        elif command == '-':
            print(number1 - number2)
        elif command == '*':
            print(number1 * number2)
        elif command == '/':
            print(number1 / number2)
    except:
        print('Error')