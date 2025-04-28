
import random


while True:
    secret = random.randint(1, 1000)
    guess = None

    while guess != secret:
        try:
            guess = int(input("Guess a number between 1 and 1000: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess > secret:
            print("Too high!")
        elif guess < secret:
            print("Too low!")
        else:
            print("You guessed it!")

    play_again = input("Do you want to play again? yes/no ").lower()
    if play_again != 'yes':
        print('Thanks for playing! See you next time.')
        break
