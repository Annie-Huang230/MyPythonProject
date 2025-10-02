"""
File: StoneMasonKarel.py
Name: Annie Huang
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will move up and down to fix columns.
    """

    up()
    down()
    cross()


def up():
    """
    pre-condition: Karel is at the bottom, facing east.
    post-condition: Karel is on the top, facing, south.
    """
    turn_left()
    while facing_north():
        if on_beeper():
            move()
        else:
            put_beeper()
        if not front_is_clear():
            turn_around()
    if not on_beeper():
        put_beeper()


def turn_around():
    turn_left()
    turn_left()


def down():
    """
    pre-condition: Karel is on the top, facing south.
    post-condition: Karel is at the bottom, facing east.
    """
    while facing_south():
        move()
        if not front_is_clear():
            turn_left()
            cross()
            up()


def cross():
    """
    pre-condition: Karel is on the column, facing east.
    post-condition: Karel is crossing to another column, facing east.
    """
    while not front_is_clear():
        pass
    for i in range(4):
        move()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
