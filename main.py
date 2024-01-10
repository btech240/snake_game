# Import needed modules
import time
from turtle import Screen

from food import Food
from snake import Snake

# Creat starting variables
game_is_on = True

# Create screen and configure
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# Create snake body
snake = Snake()
food = Food()

# Create listener events for controlling the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move snake
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()


# Create snake food


# Detect collision with food


# Create a scoreboard


# Detect collision with wall


# Detect collision with tail


# Prevent exit until click
screen.exitonclick()
