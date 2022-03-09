import turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.show_scoreboard()

    def show_scoreboard(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def update_scoreboard(self):
        self.level += 1
        self.show_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Courier", 36, "normal"))
