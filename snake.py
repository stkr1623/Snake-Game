from turtle import Turtle
class Snake:
    def __init__(self):

        self.snake_body = []
        self.new_snake()
        self.head = self.snake_body[0]

    def new_snake(self):

            for i in range(3):

                new_turtle = Turtle(shape="square")
                new_turtle.color("white")
                # new_turtle.pensize(20)
                new_turtle.penup()
                new_turtle.setx(-20 * i)
                self.snake_body.append(new_turtle)
    def move(self):
            for segment in range(len(self.snake_body) - 1, 0, -1):
                new_x = self.snake_body[segment - 1].xcor()
                new_y = self.snake_body[segment - 1].ycor()
                self.snake_body[segment].goto(new_x, new_y)
            self.snake_body[0].forward(20)
    def add_segments(self,postion):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(postion)
        self.snake_body.append(new_segment)
    def extend(self):
        self.add_segments(self.snake_body[-1].position())

    def reset_snake(self):
        for seg in self.snake_body:
            seg.goto(1000,1000)
        self.snake_body.clear()
        self.new_snake()
        self.head = self.snake_body[0]

    def up(self):
        if self.snake_body[0].heading() == 270:
            pass
        else:
            self.snake_body[0].setheading(90)

    def down(self):
        if self.snake_body[0].heading() == 90:
            return 0
        else:
            self.snake_body[0].setheading(270)
    def left(self):
        if self.snake_body[0].heading() == 0:
            pass
        else:
            self.snake_body[0].setheading(180)

    def right(self):
        if self.snake_body[0].heading() == 180:
            pass
        else:
            self.snake_body[0].setheading(0)

    
