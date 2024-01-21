import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game by Jelly")
screen.tracer(0)

snake = Snake()
food = Food()
# Create a scoreboard
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = Scoreboard()
game_over.clear()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.add_tail()
        food.refresh()
        scoreboard.add_point()

    # Detect collision with wall
    if (
            snake.head.xcor() > 290
            or snake.head.xcor() < -290
            or snake.head.ycor() > 290
            or snake.head.ycor() < -290
    ):
        snake.reset()
        scoreboard.reset()

    # Detect collision with tail
    for s in snake.snake_body[1:]:
        if snake.head.distance(s) < 10:
            snake.reset()
            scoreboard.reset()


screen.exitonclick()
