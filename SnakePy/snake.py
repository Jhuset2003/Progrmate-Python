from turtle import Turtle


POSITIONS = [(0,0),(-20,0),(-40,0)] 
ARRIBA = 90
ABAJO = 270
IZQUIERDA = 180
DERECHA = 0

class Snake:
    

    def __init__(self):
        self.segments = [] #atributo
        self.create_snake() #metodo
        self.head = self.segments[0]

    
#creacion cuerpo de serpiente
    def create_snake(self):  
        for position in POSITIONS:
            self.add_segments(position)
            
    def add_segments(self, position):
            snake_segment = Turtle("square")
            snake_segment.penup()
            snake_segment.color("white")
            snake_segment.goto(position)
            self.segments.append(snake_segment)

    def extend(self):
        self.add_segments(self.segments[-1].position())
        
        '''
        for segment in segments:
            segment.forward(20) 
        '''
    def move(self):
        #movimiento de la serpiente
        for seg_num in range(len (self.segments) - 1,0,-1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(20)
        #segments[0].left(90)
    
    def up(self):
        if self.head.heading () != ABAJO:
            self.head.setheading(ARRIBA) 
    def down(self):
        if self.head.heading () != ARRIBA:
            self.head.setheading(ABAJO) 
    def right(self):
        if self.head.heading () != IZQUIERDA:
            self.head.setheading(DERECHA) 
    def left(self):
        if self.head.heading () != DERECHA:
            self.head.setheading(IZQUIERDA) 
    '''
    snake_segment = Turtle("square")
    snake_segment.color("white")


    snake_segment3 = Turtle("square")
    snake_segment3.color("white")
    snake_segment3.goto(-40,0)
    '''


