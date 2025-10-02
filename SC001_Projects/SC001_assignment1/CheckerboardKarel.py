"""
File: CheckerboardKarel.py
Name: Annie Huang
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will draw a checkerboard in any worlds.
    """
    go()
    back()


def go():
    """
    pre-condition: Karel is at (1,1), facing east.
    post-condition: Karel is at the end of the avenue, facing north.
    """
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    turn_left()
    back()


def back():
    """
    pre-condition: Karel is at the end of the avenue, facing north.
    post-condition: Karel is at the first avenue, facing east.
    """
    while facing_north():
        if front_is_clear():
            if on_beeper():
                move()
                turn_left()
            else:
                move()
                put_beeper()
                turn_left()

    while front_is_clear():
        if on_beeper():
            move()
            if front_is_clear():
                move()
                put_beeper()
        else:
            move()
            put_beeper()
    turn_right()

    while front_is_clear():
        move()
        turn_right()
        go()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
