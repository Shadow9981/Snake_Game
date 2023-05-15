from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_body.append(new_segment)

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].goto(self.snake_body[i - 1].xcor(), self.snake_body[i - 1].ycor())
        self.snake_body[0].forward(20)

    def move_up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def move_left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def move_right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def move_down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def grow(self):
        self.add_segment(self.snake_body[-1].position())

    def reset(self):
        for segments in self.snake_body:
            segments.hideturtle()
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
