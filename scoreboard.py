from turtle import Turtle


class ScoreCard(Turtle):

    def __init__(self, l_score, r_score):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-100, 240)
        self.write(l_score, False, "center", ('Arial', 40, 'normal'))
        self.goto(100,240)
        self.write(r_score, False, "center", ('Arial', 40, 'normal'))

    def update(self, l_score, r_score):
        self.clear()
        self.goto(-100, 240)
        self.write(l_score, False, "center", ('Arial', 40, 'normal'))
        self.goto(100, 240)
        self.write(r_score, False, "center", ('Arial', 40, 'normal'))
