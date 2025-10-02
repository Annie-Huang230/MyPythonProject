"""
File: draw_line.py
Name: Annie Huang
-------------------------
This file places a dot on odd clicks and draws a line on even clicks.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow()

SIZE = 20
count = 0
dot = None
start_x = 0
start_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    """
    Function triggered by a mouse click. Draws a circle at the first click,
    then draws a line from the circle's position to the second click.
    """
    global count, dot, start_x, start_y

    count += 1

    if count % 2 != 0:
        # Save the mouse click position for the first click, and create a dot
        start_x = mouse.x
        start_y = mouse.y
        dot = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        window.add(dot)
    else:
        # When count is even, draw a line and remove the dot
        line = GLine(start_x, start_y, mouse.x, mouse.y)
        window.remove(dot)
        window.add(line)


if __name__ == "__main__":
    main()
