# Author MB 03/18/2022

import turtle

window = turtle.Screen()
window.setup(1000, 1000)
window.screensize(800, 800)
window.title("lab 4")

murtle = turtle.Turtle()
murtle.shape("turtle")
murtle.pensize(15)
murtle.color("black")
murtle.pencolor("red")
murtle.penup()
murtle.goto(100,100)
murtle.pendown()
murtle.forward(100)
murtle.right(90)
murtle.forward(100)
murtle.right(90)
murtle.forward(100)
murtle.right(90)
murtle.forward(100)

window.mainloop()