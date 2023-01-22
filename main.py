import time
from turtle import Screen,Turtle
from snake import Snake
from food import Food
from score import Score


screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


 #Detect the distance and collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.inc_score()


 #Detect collision with the wall
    if snake.head.xcor()> 280 or snake.head.xcor()<-300 or snake.head.ycor() >300 or snake.head.ycor() <-280:
        game_is_on=False
        scoreboard.game_over()


  #DEtect collioon with the tail.
  #if head collid with any segment
    for segment in snake.segment[1:]:

        if snake.head.distance(segment)< 10:
            game_is_on=False
            scoreboard.game_over()





screen.exitonclick()