"""
File: coin_flip_runs.py
Name: Annie Huang
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
    """
    This program simulates coin flips and counts the number of consecutive runs of 'H' or 'T'.
    A 'run' is defined as consecutive results of either 'H' or 'T'.
    The program continues flipping coins until the specified number of runs (input by the user) is reached.
    """
    print("Let's flip a coin!")
    run_num = int(input('Numbers of runs: '))  # The number of runs users want to simulate
    run = 0
    can_add = True  # To control if a run can be added (to avoid counting consecutive runs multiple times)

    # First flip
    coin1 = r.randint(1, 2)  # Generate a random number, 1 for 'H' and 2 for 'T'
    if coin1 == 1:
        print('H', end='')
    if coin1 == 2:
        print('T', end='')

    # Start a loop to simulate subsequent coin flips and count the runs
    while True:
        if run == run_num:  # If the number of runs reaches the user-specified run_num, exit the loop
            break
        # Simulate the next coin flip
        else:
            coin2 = r.randint(1, 2)
            if coin2 == 1:
                print('H', end='')
            if coin2 == 2:
                print('T', end='')

            if coin1 == coin2:  # if the current flip(coin2) matches the previous flip(coin1), run will be added 1 time.
                if can_add:
                    run += 1
                    can_add = False  # Set can_add to False to prevent counting multiple consecutive runs
            else:
                can_add = True  # If the flip is different, reset can_add to True to allow for a new run
            coin1 = coin2  # Update coin1 to be the result of the current flip (coin2) for the next iteration


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
    main()
