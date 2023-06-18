
def calculator():
    operation = input('''
Please select the math operator:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    first_number = int(input('Please enter the first number: '))
    second_number = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(first_number, second_number))
        print(first_number + second_number)

    elif operation == '-':
        print('{} - {} = '.format(first_number, second_number))
        print(first_number - second_number)

    elif operation == '*':
        print('{} * {} = '.format(first_number, second_number))
        print(first_number * second_number)

    elif operation == '/':
        print('{} / {} = '.format(first_number, second_number))
        print(first_number / second_number)

    else:
        print('You have not typed a valid operator, please run the program again.')

    calculate_again()

def calculate_again():
    calculate_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calculate_again.upper() == 'Y':
        calculator()
    elif calculate_again.upper() == 'N':
        print('Thanks to use my calculator.')
    else:
        calculate_again()


#def welcome():
 #   print('Welcome to Calculator')
#welcome()
calculator()
