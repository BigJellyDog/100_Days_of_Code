from turtle import Turtle


class Scoreboard(Turtle,):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-30, 270)
        self.score_points = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score_points}", align="center", font=('Courier', 15, 'normal'))

    def add_point(self):
        self.clear()
        self.score_points += 1
        self.update_scoreboard()

    def write_game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=('Courier', 30, 'normal'))

