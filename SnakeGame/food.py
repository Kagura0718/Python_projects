import random
from turtle import Turtle

COLOR = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color(self.randomcolor())
        self.speed("fastest")

        self.refresh()

    def randomcolor(self):
        color = ""
        for i in range(6):
            color += COLOR[random.randint(0, 14)]
        return '#' + color


    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.color(self.randomcolor())
        self.goto(random_x, random_y)
