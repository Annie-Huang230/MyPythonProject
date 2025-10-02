"""
File: quadratic_solver.py
Name: Annie Huang
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
    """
    This program computes the formula ax2+bx+c=0.
    """
    print('stanCode Quadratic Solver!')
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    x = (b * b) - (4 * a * c)
    if x < 0:
        print('No real roots')
    else:
        y = math.sqrt(x)
        root = (-b + y) / 2 * a
        root_2 = (-b - y) / 2 * a
        if x == 0:
            print('One root: ' + str(root))
        else:
            print('Two roots: ' + str(root) + ',' + str(root_2))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
