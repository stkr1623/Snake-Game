import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
outline = Turtle()
outline.penup()
outline.goto(x=-290,y=255)
outline.setheading(0)
outline.hideturtle()
outline.pendown()
outline.color("red")
outline.speed("fast")
for i in range(4):
    if i==1 or i==3:
        outline.forward(540)
    else :
        outline.forward(570)
    outline.right(90)

screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:

    screen.update()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    time.sleep(0.3)
    snake.move()

    if snake.snake_body[0].distance(food) < 15 :
        snake.extend()
        scoreboard.increase_score()
        food.refresh()
    if snake.snake_body[0].xcor()>=283 or snake.snake_body[0].xcor()<=-290 or snake.snake_body[0].ycor()>=260 or snake.snake_body[0].ycor()<=-285 :
        scoreboard.reset_game()
        snake.reset_snake()
    for segment in snake.snake_body[1:]:
        if snake.snake_body[0].distance(segment) <10:
            scoreboard.reset_game()
            snake.reset_snake()

screen.exitonclick()