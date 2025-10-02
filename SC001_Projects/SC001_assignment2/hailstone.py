"""
File: hailstone.py
Name: Annie Huang
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

EXIT = 1


def main():
    """
    This program computes Hailstone sequences.
    """
    print('This program computes Hailstone sequences.')
    print('')
    n = int(input('Enter a number: '))
    step = 0
    while True:
        if n == EXIT:
            break
        else:
            step += 1
            if n % 2 == 0:
                n1 = n // 2
                print(str(n) + ' is even, so I take half: ' + str(n1))
                n = n1
            else:
                n2 = (n * 3) + 1
                print(str(n) + ' is odd, so I make 3n+1: ' + str(n2))
                n = n2
    print('It took ' + str(step) + ' step(s) to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
