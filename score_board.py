from turtle import Turtle

POSITION = (-280, 260)
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(POSITION)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT)

    def increment_level(self):
        self.level += 1
        self.update_level()

    def end_game(self):
        self.goto(-60,0)
        self.write(arg="GAME OVER", font=FONT)