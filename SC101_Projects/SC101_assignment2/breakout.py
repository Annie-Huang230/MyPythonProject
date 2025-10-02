"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This code implements a Breakout game where a player controls a paddle to bounce a ball.
The goal is to break all the bricks while avoiding losing the ball.
The player has a limited number of lives, and the game ends when all bricks are destroyed
or the player runs out of lives.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10        # 100 frames per second
NUM_LIVES = 3		# Number of attempts


def main():
    lives = NUM_LIVES
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    while lives > 0 and graphics.brick_count != 0:
        # Get the current velocities (dx, dy) from BreakoutGraphics
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx, dy)

        # Check for collisions at the four corners of the ball
        collisions1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        collisions2 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.height, graphics.ball.y)
        collisions3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
        collisions4 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.height, graphics.ball.y + graphics.ball.height)

        if collisions1 is not None:
            if collisions1 is graphics.paddle:
                dy = -dy
                graphics.set_dy(dy)
            else:
                graphics.brick_count -= 1
                graphics.window.remove(collisions1)
                dy = -dy
                graphics.set_dy(dy)
        elif collisions2 is not None:
            if collisions2 is graphics.paddle:
                dy = -dy
                graphics.set_dy(dy)
            else:
                graphics.brick_count -= 1
                graphics.window.remove(collisions2)
                dy = -dy
                graphics.set_dy(dy)
        elif collisions3 is not None:
            if collisions3 is graphics.paddle:
                dy = -dy
                graphics.set_dy(dy)
            else:
                graphics.brick_count -= 1
                graphics.window.remove(collisions3)
                dy = -dy
                graphics.set_dy(dy)
        elif collisions4 is not None:
            if collisions4 is graphics.paddle:
                dy = -dy
                graphics.set_dy(dy)
            else:
                graphics.brick_count -= 1
                graphics.window.remove(collisions4)
                dy = -dy
                graphics.set_dy(dy)

        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            dx = -dx
            graphics.set_dx(dx)  # Update dx after bounce
        if graphics.ball.y <= 0:
            dy = -dy
            graphics.set_dy(dy)  # Update dy after bounce

        # Ball falls below the paddle, lose a life and reset the ball
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            lives -= 1
            graphics.restart_ball()

        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
