import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Please guess a number between 1 and {x}: '))
        if guess < random_number:
            print(f'Sorry guess again {guess} is too low')
        elif guess > random_number:
            print(f'Sorry guess again {guess} is too hight')

    print(f'Congratulations you guessed the correct number {random_number}')

def compute_guess(x)
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'It {guess} to high (H), to low (L), or correct')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l';
            low = guess + 1

    print(f'The Computer guessed your number {guess} correctly')

guess(10)