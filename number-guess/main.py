import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Please guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry guess again' + guess + 'is too low')
        elif guess > random_number:
            print('Sorry guess again' + guess + 'is too hight')

print(f'Congratulations you guessed the correct number {random_number}')

guess(10)