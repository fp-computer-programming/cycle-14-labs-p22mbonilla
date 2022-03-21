# Author MB 03/21/2022

import turtle

def move_forward():
    toby.forward(50)
window = turtle.Screen()
toby = turtle.Turtle()
window.onkey(move_forward, "Up")
window.listen()

def move_backward():
    toby.back(50)
window = turtle.Screen()
toby = turtle.Turtle()
window.onkey(move_backward, "Down")
window.listen()

def move_left():
    toby.left(45)
window = turtle.Screen()
toby = turtle.Turtle()
window.onkey(move_left, "Left")
window.listen()

def move_right():
    toby.right(45)
window = turtle.Screen()
toby = turtle.Turtle()
window.onkey(move_right, "Right")
window.listen()

window.mainloop()
