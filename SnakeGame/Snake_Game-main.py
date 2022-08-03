from turtle import Screen
import time
from food import Food
from Snakes import Snake
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detection of collision with wall.
    if snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() > 290:
        game_is_on = False
        score.game_over()
    # detect collision with food
    if snake.head.distance(food) < 15:
        score.increase_score()
        score.update_score()
        snake.extend()
        food.new_position()
    # Detect collision with tail
    for i in snake.segments[1:]:
        if snake.head.distance(i) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
