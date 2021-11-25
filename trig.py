import random,turtle,math


screen=turtle.Screen()
drawer = turtle.Turtle()
dotter=turtle.Turtle()
axis = turtle.Turtle()
axis.pencolor("blue")
axis.goto(0,0)
axis.forward(500)
axis.left(180)
axis.forward(500*2)
axis.goto(0,0)
axis.left(90)
axis.forward(500)
axis.left(180)
axis.forward(500*2)
axis.hideturtle()

dotter.pencolor("green")
dotter.penup()
drawer.speed(1)

hypo=250
times=5
for i in range (times):
    print(i)
    adj=random.randint(0,50)
    op= hypo**2-adj**2
    op=math.sqrt(op)
    x= math.asin(op/hypo)
    y= (x*180)/math.pi+90
    print("opo:"+str(op),"hype;"+str(hypo),"adja;"+str(adj),"angle"+ str(y))

    drawer.forward(adj)
    dotter.pencolor("yellow")
    dotter.goto(drawer.xcor(),drawer.ycor())
    dotter.dot(10)
    dotter.penup()


    drawer.left(90)
    drawer.forward(op)
    print(drawer.xcor(),drawer.ycor())
    dotter.pencolor("green")
    dotter.goto(drawer.xcor(),drawer.ycor())
    dotter.dot(10)
    dotter.penup()


    drawer.left(y)
    drawer.forward(hypo)
    #print(drawer.xcor(),drawer.ycor())
    dotter.pencolor("red")
    dotter.goto(drawer.xcor(),drawer.ycor())
    dotter.dot(10)
    dotter.penup()



turtle.done()
