"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This class defines the BreakoutGraphics object, which initializes the game components such as
the paddle, ball, and bricks. It also handles user interaction (mouse events) and provides methods
to control the game's behavior, like resetting the ball or moving the paddle.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10      # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 100      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)//2, y=self.window.height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)//2, y=(self.window.height-self.ball.height)//2)

        # Total number of bricks
        self.brick_count = brick_rows * brick_cols

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_move)

        # Control whether the mouse can be clicked
        self.can_click = True

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                x = i * (brick_width + brick_spacing)
                y = j * (brick_height + brick_spacing) + brick_offset
                self.brick = GRect(brick_width, brick_height, x=x, y=y)
                self.brick.filled = True

                # Assign a color to the brick based on its row. 5 colors are distributed into brick_rows
                if brick_rows < 5:  # Handle cases with fewer than 5 rows
                    if j == 0:
                        self.brick.fill_color = 'red'
                    if j == 1:
                        self.brick.fill_color = 'orange'
                    if j == 2:
                        self.brick.fill_color = 'yellow'
                    if j == 3:
                        self.brick.fill_color = 'green'
                    if j == 4:
                        self.brick.fill_color = 'blue'
                else:
                    if j // (brick_rows // 5) == 0:
                        self.brick.fill_color = 'red'
                    elif j // (brick_rows // 5) == 1:
                        self.brick.fill_color = 'orange'
                    elif j // (brick_rows // 5) == 2:
                        self.brick.fill_color = 'yellow'
                    elif j // (brick_rows // 5) == 3:
                        self.brick.fill_color = 'green'
                    elif j // (brick_rows // 5) == 4:
                        self.brick.fill_color = 'blue'
                self.brick.color = self.brick.fill_color  # Set the border color to be the same as the filled color
                self.window.add(self.brick)

    def ball_move(self, mouse):
        """
        Starts the ball movement when the user clicks.
        Ensures the ball moves only after the first click.
        """
        if self.can_click:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.can_click = False  # Prevent further clicks

    def restart_ball(self):
        """
        Resets the ball to the center of the window and stops its movement.
        """
        self.ball.x = (self.window.width-self.ball.width)//2
        self.ball.y = (self.window.height-self.ball.height)//2
        self.__dx = 0
        self.__dy = 0
        self.can_click = True  # Allow the ball to be launched again

    def paddle_move(self, mouse):
        """
        Moves the paddle horizontally based on the mouse's position.
        Ensures the paddle stays within the window boundaries.
        """
        new_x = mouse.x - self.paddle.width // 2  # Calculate the paddle's new x position
        if new_x < 0:
            new_x = 0
        elif new_x + self.paddle.width > self.window.width:
            new_x = self.window.width - self.paddle.width
        self.paddle.x = new_x  # Update the paddle's x position

    def get_dx(self):
        """
        :return: the current horizontal velocity of the ball.
        """
        return self.__dx

    def get_dy(self):
        """
        :return: the current vertical velocity of the ball.
        """
        return self.__dy

    def set_dx(self, new_dx):
        """
        Sets a new horizontal velocity for the ball.
        """
        self.__dx = new_dx

    def set_dy(self, new_dy):
        """
        Sets a new vertical velocity for the ball.
        """
        self.__dy = new_dy



