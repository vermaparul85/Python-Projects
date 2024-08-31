from IPython.display import clear_output
from art import calc_logo
import sys

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Using function as variable
calc_dict = {'+': add, '-': subtract, '*': multiply, '/': divide}

def calculator():
    print(calc_logo)
    first_number = float(input('What is your first number? '))
    
    while True:
        for symbol in calc_dict:
            print(symbol)
        operation = input('Pick an operation? ')
        next_number = float(input('What is your next number? '))
        
        result = calc_dict[operation](first_number,next_number)
        print(f'{first_number} {operation} {next_number} = {result}')
        
        continue_calculating = input(f'Type "y" to continue calculating with {result}, or type "n" to start a new calculation: ').lower()
    
        if continue_calculating == 'y':
            first_number = result
        else:
            clear_output()

            new_operation = input(f'Do you want to continue? Type "y" or "n": ').lower()
            if new_operation == 'n':
                print('Bye Bye')
                sys.exit(0)
            elif new_operation == 'y':
                calculator()             # Using recursion

calculator()
