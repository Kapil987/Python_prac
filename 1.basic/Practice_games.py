## shift + selct line + tab and select line + tab to indent and undo indent
## Alt click for multi select and then replace or edit
## User play with computer
# import random
# def guess(x):
#     random_number = random.randint(1,x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'Guess a number btw 1 and {x}:: ')) # 4
#         if guess < random_number:
#             print('Sorry, guess again. Too Low.')
#         elif guess > random_number:
#             print('Sorry, guess again, Too High. ')
#     print(f'Yay, congrats. You have guess the number {random_number} correctly ')

# guess(10)

## Computer play with user
# import random
# def comput_guess(x):
#     low = 1
#     high = x
#     feedback = ''
#     while feedback != 'c':#and low != high:
#         if low != high:
#             guess = random.randint(low,high)
#         else:
#             guess = low
#         # guess = random.randint(low,high)
#         feedback = input(f'Is {guess} too high (H), too low (L), or correct (C) ??').lower()
#         if feedback == 'h':
#             high = guess -1
#         elif feedback == 'l':
#             low = guess +1
#     print(f'Yay, congrats. Computer have guess the number {guess} correctly!')

# comput_guess(10)

# import random
# def comput_guess(x):
#     low = 1
#     high = x
#     feedback = ''
#     while feedback != 'c':
#         # if low != high:
#         #     guess = random.randint(low,high)
#         # else:
#         #     guess = low
#         guess = random.randint(low,high) # guess == 5 and input is also 5
#         feedback = input(f'Is {guess} too high (H), too low (L), or correct (C) ??').lower()
#         if feedback == 'h':
#             high = guess -1
#         elif feedback == 'l':
#             low = guess +1
#     print(f'Yay, congrats. Computer have guess the number {guess} correctly!')

# comput_guess(2)

## Rock paper sccisor
# import random

# def play():
#     user = input("Whats your choice? \n'r' for rock, \n'p' for paper, \n's' for scissors:: \n")
#     computer = random.choice(['r','p','s'])

#     if user == computer:
#         return 'It\'s Tie'
#     if is_win(user,computer):
#         return 'You Win!'
    
#     return 'You Lost!'
# # r > s, s > p, p > r
# def is_win(player,opponent):
#     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or \
#         (player == 'p' and opponent == 'r'):
#         return True  

# print(play())