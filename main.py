from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_running = True

while game_running:
    screen.update()
    time.sleep(0.1)

    snake.move()

    screen.listen()
    screen.onkeypress(key="Up", fun=snake.move_up)
    screen.onkeypress(key="Left", fun=snake.move_left)
    screen.onkeypress(key="Right", fun=snake.move_right)
    screen.onkeypress(key="Down", fun=snake.move_down)

    if snake.snake_body[0].distance(food) < 15:
        snake.grow()
        scoreboard.increase_score()
        food.refresh()

    if snake.snake_body[0].xcor() < -290 or snake.snake_body[0].xcor() > 290 or snake.snake_body[0].ycor() < -290 or snake.snake_body[0].ycor() > 290:
        game_running = False
        scoreboard.game_over()

    for segment in snake.snake_body[1::]:
        if snake.snake_body[0].distance(segment) < 10:
            game_running = False
            scoreboard.game_over()

screen.exitonclick()
