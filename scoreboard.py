from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('C:/Users/shubh_zbleutb/OneDrive/Desktop/data.txt') as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align='center', font=('Arial', 24, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('C:/Users/shubh_zbleutb/OneDrive/Desktop/data.txt', mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, align='center', font=('Arial', 24, 'normal'))
