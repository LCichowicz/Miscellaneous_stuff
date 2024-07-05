#Simple guessing game. User have to guess a number from 1-10 in as little attempts as possible.
from random import randint


def number_validation(number:str)->int:
    try:
        number = int(number)
    except ValueError:
        print('You have to give a valid intiger next time!!!')
        quit()

    return number




print("Guess the number :)")
level = input('Give a number of Your choice: ')

level = number_validation(level)
try:
    roll = randint(1,level)
except ValueError:
    print('You have to give a number greater than 0')
    quit()

print('Rolls have been diced :)')

counter = 1
while True:
    user_guess = input(f'Pick a number from 1 to {level}: ')
    user_guess = number_validation(user_guess)

    if user_guess < roll:
        print("You should aim higher")
    elif user_guess > roll:
        print('Aim a bit lower')
    
    if roll != user_guess:
        print('You missed :(')
        
        counter += 1
    else:
        break


if counter ==1 :
    attempt = 'attempt'
else:
    attempt = 'attempts'

print(f'Correct answer is {roll}')
print(f"Congratulations!!! You guessed with {counter} {attempt}!!")
