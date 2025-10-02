"""
File: hangman.py
Name: Annie Huang
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman game.
    """
    ans = random_word()
    d = dashed(ans)
    previous_guess = d

    print('The word looks like: ' + d)
    print('You have ' + str(N_TURNS) + ' wrong guesses left.')

    count = N_TURNS
    while count > 0 and previous_guess != ans:
        input_ch = input('Your guess: ')
        if not input_ch.isalpha() or len(input_ch) > 1:
            print('Illegal format')
        else:
            upper = ''
            if input_ch.islower():  # change lowercase to uppercase
                upper += input_ch.upper()
            else:
                upper = input_ch
            if upper in ans:  # check if the guess is in the ans
                dash = check(ans, upper, previous_guess)
                previous_guess = dash
                print('You are correct!')
            else:
                count -= 1  # if guess is wrong, count - 1
                print('There is no ' + upper + "'s " + 'in the word.')
            if count >= 1 and previous_guess != ans:
                print('The word looks like: ' + previous_guess)
                print('You have ' + str(count) + ' wrong guesses left.')
    if previous_guess != ans:
        print('You are completely hung :(')
    else:
        print('You win!!')

    print('The answer is: ' + ans)


def dashed(ans):
    """
    :return: str, dash of the random word
    """
    d = ''
    for i in range(len(ans)):
        d += '-'
    return d


def check(ans, upper, previous_guess):
    """
    :return: str, dash and correct alpha from previous guesses
    """
    dash = ''
    for i in range(len(ans)):
        ch = ans[i]
        if ch == upper:
            dash += upper
        elif previous_guess[i].isalpha():
            dash += previous_guess[i]
        else:
            dash += '-'
    return dash


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
