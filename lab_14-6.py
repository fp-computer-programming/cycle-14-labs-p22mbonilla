# Author MB 03/21/2022

import turtle

window = turtle.Screen()
murtle = turtle.Turtle()

def change_color(color):
    murtle.pencolor(color)

def change_size(size):
    murtle.pensize(size)

def make_square():
    murtle.forward(125)
    murtle.right(90)
    murtle.forward(125)
    murtle.right(90)
    murtle.forward(125)
    murtle.right(90) 
    murtle.forward(125)
    


change_color(window.textinput("color", "enter a color"))
change_size(window.textinput("size", "enter a size"))
window.onclick(make_square(), btn = 1)
window.listen()

window.mainloop()