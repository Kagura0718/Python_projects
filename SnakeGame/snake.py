from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # start= len(segments)-1 , stop= 0, step= -1
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # head is segments[0], which is "Turtle" and turtle has heading(), which gives a direction
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def update(self):
        if self.head.heading() == UP:
            x = self.head.xcor()
            y = self.head.ycor() + 20
        if self.head.heading() == DOWN:
            x = self.head.xcor()
            y = self.head.ycor() - 20
        if self.head.heading() == RIGHT:
            x = self.head.xcor() + 20
            y = self.head.ycor()
        if self.head.heading() == LEFT:
            x = self.head.xcor() - 20
            y = self.head.ycor()

        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto((x, y))
        new_segment.left(self.head.heading())
        self.segments.insert(0, new_segment)
        self.head = self.segments[0]
