from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.goto(0, 260)

        self.color("white")
        self.penup()
        self.style = ('Courier', 30, 'bold')
        self.hideturtle()

        self.write("Score: " + str(self.score),
                   font=self.style, align="center")

    def add_score(self):
        # Clear the scoreboard before updating and re-writing
        self.clear()
        self.score += 1
        self.write("Score: " + str(self.score),
                   font=self.style, align="center")
