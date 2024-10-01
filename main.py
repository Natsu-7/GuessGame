# Guess the number

import random

target_number = random.randint(1, 100)
print(target_number)

count = 5      # the number of tries the user has

while count != 0:
    guess_number = int(input('Enter a number between 1 to 100 : '))
    if guess_number != target_number:
        count -= 1
        if guess_number > target_number:
            print(f'{guess_number} is higher than the target number')
        elif guess_number < target_number:
            print(f'{guess_number} is lower than the target number')
    elif guess_number == target_number:
        print('Congratulations !!!!! YOU WON ! YOU GUESSED THE CORRECT ANSWER')
        break
else:
    print(" YOU LOST")
