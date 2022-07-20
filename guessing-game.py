import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = (input("Guess a random number: "))
        if guess > random_number:
            print("your guess is too high")
        elif guess < random_number:
            print("your guesss is too low")
            print("your guess is right")
            guess(10)


