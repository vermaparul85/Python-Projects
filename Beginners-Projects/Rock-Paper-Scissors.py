import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
          _______)
      (____)
---.__(___)
'''

game_diaplay = [rock, paper, scissors]

while True:
    players_choice = int(input('What do you choose? type 0 for Rock, 1 for Paper, or 2 for Scissors \n'))

    if players_choice not in [0,1,2]:
        continue
    else:
        break
        
print(game_diaplay[players_choice])

computer_choice = random.randint(0,2)

print('Computer chose:')
print(game_diaplay[computer_choice])

if players_choice == computer_choice:
    print('No one wins. Play again')
elif players_choice == 0 and computer_choice == 2:
    print('You win')
elif computer_choice > players_choice:
    print('You lose')
elif computer_choice == 0 and players_choice == 2:
    print('You lose')
elif players_choice > computer_choice:
    print('You win')
