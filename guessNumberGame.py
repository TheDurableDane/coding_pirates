import random


number_low = 1
number_high = 100
number = random.randint(number_low, number_high)

wrong_answer = True
n_guesses = 0
while wrong_answer:
    guess = int(input("Guess a number between {0} and {1}: ".format(number_low, number_high)))
    n_guesses += 1

    if guess == number:
        print("Gratz, m8. You won using only {0} guesses.".format(n_guesses))
        wrong_answer = False
    elif guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
