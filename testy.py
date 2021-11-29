import random
import turtle

screen = turtle.Screen()
turtle = turtle.Turtle()


def move():
    turtle.ontimer(1000)
    turtle.goto(random.randint(0, 800080))


for i in range(5000):
    move()
