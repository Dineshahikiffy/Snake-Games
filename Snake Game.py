from turtle import *
from random import randrange# used for thye position of the food in the turtle window
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Changing snake direction in turtle window
def change(x, y):
    aim.x = x
    aim.y = y

# Keeping snake within a turtle window layout
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

# Moving the snake in turtle window
def move():
    head = snake[-1].copy()
    head.move(aim)
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'yellow') # This method we can written for the when the snake is byte them-self and touch the layout of the turtle window the game will over
        update()
        update()
        bgcolor('black')
        write("Game Over", align="center", font=("Courier", 36, "normal"))
        return

    snake.append(head)

    # Food and Snake increment in the turtle window
    if head == food:
        print("Snake", len(snake) - 1)
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    # Drawing the game lines in turtle window
    for body in snake:
        square(body.x, body.y, 9, 'red')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)


# Setting up the game window heigtht and width in and hide the cursor in a turtle window
setup(420, 420, 370, 0)
hideturtle()
tracer(False)

# Adding Keyboard Controls the snakes using lambda functiona
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

bgcolor('black')# background colour for the turtle window in game space
move()
done()
