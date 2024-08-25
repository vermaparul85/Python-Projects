import string
from art import caesar_logo

def caesar(encode_decode, message, shift_number):
    output = ''
    for letter in message:
        if letter not in string.ascii_lowercase:
            output += letter
        else:
            alphabet_index = string.ascii_lowercase.index(letter)
        
            if encode_decode == 'encode':
                new_index = alphabet_index + shift_number
            else:
                new_index = alphabet_index - shift_number
    
            new_index %= len(string.ascii_lowercase)
            output += string.ascii_lowercase[new_index]
    return output
    
print(caesar_logo)

replay = True
while replay:
    encode_decode = input('Type "encode" to encrypt, "decode" to decrypt:\n').lower()
    message = input('Type your message:\n').lower()
    shift_num = int(input('Type the shift number:\n'))
    
    output = caesar(encode_decode, message, shift_num)
    print(f'Here is your {encode_decode}d message: {output}')
    
    restart = input('Type "yes" if you want to go again, otherwise type "no"').lower()

    if restart == 'no':
        replay = False