import random
import string


def guessing_game():
    correct_num = 0
    incorrect_num = 0
    count_guesses = 0

    while True:
        guess = input('Guess a number between 1~10: ')
        number = random.randint(1, len(string.digits))
        # number = 3
        count_guesses += 1
        if guess.lower() == 'exit':
            print(f'Correct guess {correct_num} times, wrong guess {incorrect_num} times out of all {count_guesses} guesses')
            if correct_num >= 5:
                print(f'You have passed the test and got {correct_num}/{len(string.digits)}!')
            break
        
        if int(guess) == number:
            correct_num += 1
            print(f'Hooray! You are Success {number} and you got correct {correct_num} times')
            continue
        else:
            incorrect_num += 1
            print(f'Oops! the correct number was {number} and you failed {incorrect_num} times')
            continue

guessing_game()