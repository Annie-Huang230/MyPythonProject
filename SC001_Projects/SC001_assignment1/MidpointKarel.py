"""
File: MidpointKarel.py
Name: Annie Huang
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will be at the midpoint in any worlds.
    """
    go()
    put_and_pick()
    one_beeper_mid()


def go():
    """
    pre-condition: Karel is at (1,1), facing east.
    post-condition: Karel is at the end of avenue, facing west.
    """
    if front_is_clear():
        put_beeper()
    while front_is_clear():
        move()
    turn_around()
    put_beeper()


def put_and_pick():
    """
    pre-condition: Karel is at the end of avenue, facing west.
    post-condition: The number of beepers at the midpoint is 2.
    """

    while front_is_clear():
        move()
        if on_beeper():
            pick_beeper()
            turn_around()
            move()
            put_beeper()
    turn_around()


def one_beeper_mid():
    """
    pre-condition: The number of beepers at the midpoint is 2.
    post-condition: Only 1 beeper at the midpoint is 1.
    """
    while front_is_clear():
        move()
        if on_beeper():
            pick_beeper()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
