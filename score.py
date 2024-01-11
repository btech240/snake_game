from turtle import Turtle

ALIGNMENT = "center"
STYLE = ('Courier', 30, 'bold')


class Score(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {str(self.score)}", font=STYLE, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=STYLE, align=ALIGNMENT)

    def add_score(self):
        # Clear the scoreboard before updating and re-writing
        self.clear()
        self.score += 1
        self.update_score()
