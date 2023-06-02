from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
ANGLE = 90


class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		with open("high_score.txt") as data:
			self.high_score = int(data.read())
		self.color("white")
		self.penup()
		self.goto(0, 270)
		self.hideturtle()
		self.update_score()

	def border(self):
		self.pensize(6)
		self.penup()
		self.hideturtle()
		self.color("black")
		self.goto(-290, 290)
		# self.pendown()
		self.goto(-290, -290)
		self.goto(290, -290)
		self.goto(290, 290)
		self.goto(-290, 290)
		self.color("black")
		self.begin_fill()
		for _ in range(4):
			self.left(ANGLE)
			self.goto(-290, -290)
			self.left(ANGLE)
			self.goto(290, -290)
			self.left(ANGLE)
			self.goto(290, 290)
			self.left(ANGLE)
			self.goto(-290, 290)

		self.end_fill()
		self.color("white")

	def update_score(self):
		self.clear()
		self.goto(0, 300)
		self.write(f"Score: {self.score}                              High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
		self.penup()

	def reset(self):
		self.game_over()
		if self.score > self.high_score:
			self.high_score = self.score
			with open("high_score.txt", mode="w") as data:
				data.write(str(self.score))
		self.score = 0
		# self.update_score()

	def game_over(self):
		# self.update_score()
		self.penup()
		self.goto(0.00, 0.00)
		self.color("dark red")
		self.hideturtle()
		self.write("GAME OVER", align=ALIGNMENT, font=("Arial", 50, "normal"))
		if self.score <= self.high_score:
			self.goto(0.00, -50)
			self.write(f"Your Score: {self.score}", align=ALIGNMENT, font=("Arial", 30, "normal"))
		elif self.score > self.high_score:
			self.goto(0.00, -50)
			self.write(f"New High Score: {self.score}", align=ALIGNMENT, font=("Arial", 30, "normal"))


	def start_over(self):
		self.goto(0.00, -150)
		self.write("Press 'Spacebar' to Play Again", align=ALIGNMENT, font=("Arial", 20, "normal"))
		# self.update_score()

	def quit_game(self):
		self.goto(0, -130)
		self.write("Press 'Backspace' to Play Again", align=ALIGNMENT, font=("Arial", 20, "normal"))


	def increase_score(self):
		self.score += 1
		self.update_score()


