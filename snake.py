from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake_segment = Turtle('square')
        new_snake_segment.penup()
        new_snake_segment.color('white')
        new_snake_segment.goto(position)
        self.snake_segments.append(new_snake_segment)

    def reset(self):
        for seg in self.snake_segments:
            seg.goto(10000, 10000)
        self.snake_segments.clear()
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def extend(self):
        """here 'position()' is different from above position variable in for loop. This is a method in turtle class."""
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for seg in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg - 1].xcor()
            new_y = self.snake_segments[seg - 1].ycor()
            self.snake_segments[seg].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
