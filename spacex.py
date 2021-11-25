import time,turtle,random

screen=turtle.Screen()
screen.screensize(1000,1000)
screen.register_shape("rectangle",((-10,3),(10,3),(10,50),(-10,50)))

stage1=turtle.Turtle()
stage1.penup()
stage1.shape("rectangle")
stage1.left(90)
stage1.goto(0,-399)
stage1.color("green")
stage1.speed(0)

thrust=turtle.Turtle()
thrust.penup()
thrust.shape("circle")
thrust.color("red")
thrust.goto(0,-400)
thrust.speed(0)
thrust.left(90)


for i in range (70):
    #time.sleep(0.1)
    stage1.pendown()
    thrust.pendown()
    stage1.forward(10)
    thrust.forward(10)

print("About to deploy sattelites")
for i in range (30):
        a = turtle.Turtle()
        a.penup()
        a.speed(0)
        a.shape("square")
        a.goto(random.randint(-400,600),random.randint(400,600))

print("Returning to land")
stage1.penup()
thrust.hideturtle()
thrust.penup()
for i in range(1000,-1400,-50) :
    time.sleep(0.1)
    x = i/10.0
    y = -(x**2 )/50
    stage1.goto(x,y)
    thrust.goto(x,y)
    print(x,y)
    if(x>95):
        thrust.showturtle()
        thrust.pendown()
print("Landed")
