from turtle import Screen,Turtle
import time

#Crear el escenarios
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("programate snake")
screen.tracer(0)


#creacion cuerpo de serpiente
positions = [(0,0),(-20,0),(-40,0)]

segments = []

for position in positions:
    snake_segment = Turtle("square")
    snake_segment.penup()
    snake_segment.color("white")
    snake_segment.goto(position)
    segments.append(snake_segment)
    
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    '''
    for segment in segments:
        segment.forward(20) 
    '''
    for seg_num in range(len (segments) - 1,0,-1):
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)
    segments[0].left(90)
'''
snake_segment = Turtle("square")
snake_segment.color("white")


snake_segment3 = Turtle("square")
snake_segment3.color("white")
snake_segment3.goto(-40,0)
'''


screen.exitonclick()