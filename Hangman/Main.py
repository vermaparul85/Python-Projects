import random
from hangman_images import logo, stages
from hangman_words import word_list

print(logo)

#choose_num = random.randint(0, len(word_list)-1)
#choosen_word = word_list[choose_num]
choosen_word = random.choice(word_list)

guessed_word = ['_'] * len(choosen_word)

#print(choosen_word)
print(f"Word to guess: {' '.join(guessed_word)}")

total_lives = 6

while '_' in guessed_word:
    letter = input('Guess the letter: ').lower()

    if letter in choosen_word:
        for index,i in enumerate(choosen_word):
            if i == letter:
                guessed_word[index] = letter
    else:
        print(f'You guessed {letter}, that is not in the word. You lose a life')
        total_lives -= 1
        print(stages[total_lives])
        print(f'******************** {total_lives}/6 LIFES LEFT **************************')
    
    print(' '.join(guessed_word))

    if total_lives == 0:
        break
else:
    print('You win!!')

if '_' in guessed_word:
    print(f'Game over. You lost. The word was "{choosen_word}"')
