from turtle import Turtle
import random

COLORS = ["yellow", "blue", "orange", "pink", "purple"]
class Food(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(stretch_wid=0.5, stretch_len=0.5)
		self.color(random.choice(COLORS))
		self.speed("fastest")
		self.refresh()

	def refresh(self):
		random_x = random.randint(-280, 280)
		random_y = random.randint(-280, 280)
		self.color(random.choice(COLORS))
		self.goto(x=random_x, y=random_y)

