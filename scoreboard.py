from turtle import Turtle
ALIGBNMENT = "center"
FONT = ("Arial", 24,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.pendown()
        with open("highscore.txt") as file:
            self.highscore = int(file.read())

        self.update_score()
        self.penup()
    def update_score(self):
        self.clear()
        self.write(f"SCORE : {self.score} High Score : {self.highscore}", move=False, align=ALIGBNMENT, font=FONT)
    def reset_game(self):
        if self.score > int(self.highscore) :
            self.highscore=self.score
            with open("highscore.txt",mode="w") as file:
                file.write(f"{self.highscore}")

        self.score = 0
        self.update_score()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game over !! ", move=False, align=ALIGBNMENT, font=("Times New Roman", 35,"normal"))
    #     self.goto(0,-30)
    #     self.write(f"Your Score : {self.score}", move=False, align=ALIGBNMENT, font=("Arial", 20,"normal"))

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()