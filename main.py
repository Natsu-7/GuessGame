'''
Title : Guess the number Game
Author : Chaitanya Shah
Class : CYSE1002
Date : 9th October 2024

Description :
This is a game in which user has to guess the number between 1 to 100 .
The target number is randomly generated .
User gets 5 tries to guess the correct answer.
If guess is wrong , the small hint is provided.
'''
import random


def user_input_validation():
    '''
    Description :
    This function takes the input from the user and then validates if the input is a number or not.
    If the input is number then checks that it is between 1 to 100.
    If this condition is also true, it will return the number
    Otherwise it will display the appropriate message to user.
    This function will continue to run till the user inserts a number which is between 1 to 100
    :return:
    a number between 1 to 100
    '''
    while True:
        user_input = input('Enter a number between 1 to 100 : ')

        if user_input.isdigit():
            user_input = int(user_input)
            if 1 <= user_input <= 100:
                return user_input
            else:
                print('Please enter number between 1 to 100')
        else:
            print('Please enter a number')


target_number = random.randint(1, 100)

count = 5      # the number of tries the user has

while count != 0:
    guess_number = user_input_validation()
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
    print("The target number was", target_number)
    print("YOU LOST")
print("Thank you for Playing the game")
