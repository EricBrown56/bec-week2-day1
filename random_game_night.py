# Random game night generator
# Guess the number between 1 and 10

import random
number = range(1, 11)
random_number = random.choice(number)
guess_num = 1

guess = int(input('Guess the number between 1 and 10: '))
while guess != random_number:
    guess = int(input('Guess again: '))
    guess_num += 1
else:
    print('You guessed it! The number was:', random_number)
    print('It took you', guess_num, 'guesses')