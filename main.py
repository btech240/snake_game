# Import needed modules
from turtle import Screen, Turtle

# Create screen and configure
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


# Create snake body
starting_position = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)


# Move snake


# Create snake food


# Detect collision with food


# Create a scoreboard


# Detect collision with wall


# Detect collision with tail


# Prevent exit until click
screen.exitonclick()
