import random
import string

letters_list = []

print('Welcome to the PyPassword Generator!')
letters = int(input('How many letters would you like in your password?\n'))
symbols = int(input('How many symbols would you like?\n'))
numbers = int(input('How many numbers would you like?\n'))

for i in range(letters):
    letters_list.append(random.choice(string.ascii_letters))

for i in range(symbols):
    letters_list.append(random.choice(string.punctuation))
    
for i in range(numbers):
    letters_list.append(random.choice(string.digits))

print(letters_list)
random.shuffle(letters_list)
print(letters_list)

password = ''.join(letters_list)
print(f'Your password is: {password}')