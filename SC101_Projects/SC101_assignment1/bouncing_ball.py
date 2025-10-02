"""
File: bouncing_ball.py
Name: Annie Huang
-------------------------
This file creates a ball which bounces on the window.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
count = 0
can_click = True

dot = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(ball_move)
    dot.filled = True
    window.add(dot)


def ball_move(mouse):
    """
    Function that moves the ball when the user clicks the mouse.
    """
    global count, can_click, dot
    vy = 0
    if can_click and count < 3:
        can_click = False  # Disable further clicks until this bounce completes

        # Keep moving the ball until the ball reaches the right edge or completes its bounce
        while not can_click:
            dot.move(VX, vy)
            vy += GRAVITY
            if dot.y + SIZE >= window.height:
                vy = -vy * REDUCE
            if dot.x + SIZE > window.width:
                count += 1
                can_click = True  # Allow a new click to start another bounce
                dot.x = START_X
                dot.y = START_Y

            pause(DELAY)


if __name__ == "__main__":
    main()
