# Import needed modules
import time
from turtle import Screen, Turtle

# Creat starting variables
game_is_on = True

# Create screen and configure
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# Create snake body
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


# Move snake
while game_is_on:
    screen.update()
    time.sleep(0.2)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

# Create snake food


# Detect collision with food


# Create a scoreboard


# Detect collision with wall


# Detect collision with tail


# Prevent exit until click
screen.exitonclick()
