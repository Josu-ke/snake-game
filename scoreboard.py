from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        with open("highscore.txt", "r") as f:
            self.highscore = int(f.read())
            f.close()
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.refresh()

    def score_s(self):
         self.score += 1
         self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", "w") as f:
                f.write(str(self.score))
                f.close()
        self.score = 0
        self.refresh()