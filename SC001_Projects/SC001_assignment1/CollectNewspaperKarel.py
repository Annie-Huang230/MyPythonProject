"""
File: CollectNewspaperKarel.py
Name: Annie Huang
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will go out to pick the newspaper and come back home.
    """

    move_to_news()
    news_back_home()


def move_to_news():
    """
    pre-condition: Karel is in the house, facing East.
    post-condition: Karel is out of the house with the news, facing West.
    """
    go_out()
    pick_news()


def go_out():
    """
    pre-condition: Karel is in the house, facing East.
    post-condition: Karel is out of the house, facing East.
    """
    while front_is_clear():
        move()
    turn_right()
    move()
    while facing_south():
        if left_is_clear():
            turn_left()
            move()


def pick_news():
    """
    pre-condition: Karel is out of the house, facing East.
    post-condition: Karel is out of the house with the news, facing West.
    """
    while on_beeper():
        pick_beeper()
        turn_around()


def news_back_home():
    """
    pre-condition: Karel is out of the house with the news, facing West.
    post-condition: Karel puts the news in the house, facing East.
    """
    while front_is_clear():
        move()
    turn_right()
    while facing_north():
        move()
        turn_right()
        put_beeper()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
