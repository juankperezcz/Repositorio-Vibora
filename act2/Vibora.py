from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    #Hace que la serpiente cambie de direción
    "Change snake direction."
    aim.x = x
    aim.y = y
    #Hace que se mueva la comida cuando se mueva la comida cuando se mueva la serpiente
    food.x = randrange(-5,5) *10
    food.y = randrange(-5,5) *10

def colorRand(init):
    "Randomiza los colores"
    
    val=random.randrange(1,6) #se definen los rangos del 1 al 6 para generar un número del 1 al 5
    if val==1:
        #por cada vez que se corra el juego el color cambia. En este caso, si el número aleatorio
        #generado es 1, el color será verde y así con todos los elifs.
        color = 'red'
    elif val==2:
        color = 'blue'
    elif val==3:
        color = 'orange'
    elif val==4:
        color='pink'
    elif val==5:
        color='black'
    if color==init:
        color=colorRand(color)
    return color

snakeColor=colorRand('red') #se define el color default que se menciona en la actividad.
foodColor=colorRand(snakeColor) #se define el color de la comida de la serpiente

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    #cambia el color de la cabeza si la serpiente choca o se sale de la cuadrilla
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        #imprime la longirud de la serpiente
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()