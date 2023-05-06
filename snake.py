from turtle import Turtle


class Snake(Turtle):
    snake_body = []

    def __init__(self):
        super().__init__()
        for i in range(3):
            timmy = Turtle("square")
            timmy.color("white")
            timmy.penup()
            timmy.goto(i * -20, 0)
            self.snake_body.append(timmy)

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
        timmy = Turtle("square")
        timmy.color("white")
        timmy.penup()
        timmy.goto(self.snake_body[-1].position())
        self.snake_body.append(timmy)
