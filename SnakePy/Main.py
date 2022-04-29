from turtle import Screen,Turtle
from snake import Snake
from comida import Comida
from scoreboard import Scoreboard
import time

#Crear el escenarios
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("programate snake")
screen.tracer(0)

snake = Snake()
comida = Comida()
scoreboard = Scoreboard()


#movimientos serpiente
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    #Colision de comida
    if snake.head.distance(comida) < 15:
        comida.refresh()
        scoreboard.increased_score() 
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -295 or snake.head.ycor() > 285 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()