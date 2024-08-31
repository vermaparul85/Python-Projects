from IPython.display import clear_output
from art import calc_logo

def calculate(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2

    return result

print(calc_logo)

while True:
    first_number = float(input('What is your first number? '))

    while True:
        print('+\n-\n*\n/')
        operation = input('Pick an operation? ')
        next_number = float(input('What is your next number? '))
        result = calculate(first_number, next_number, operation)
        print(f'{first_number} {operation} {next_number} = {result}')
    
        continue_calculating = input(f'Type "y" to continue calculating with {result}, or type "n" to start a new calculation: ').lower()

        if continue_calculating == 'y':
            first_number = result
        else:
            break

    new_operation = input(f'Do you want to continue? Type "y" or "n": ').lower()

    if new_operation == 'n':
        break

    clear_output()
