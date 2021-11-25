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
drawer.speed(1000)

hypo=250
times=10
q1={}
q2={}
for i in range (times):
    print(i)
    adj=random.randint(0,250)
    op= hypo**2-adj**2
    op=math.sqrt(op)
    x= math.asin(op/hypo)
    y= (x*180)/math.pi
    #print("opo:"+str(op),"hype;"+str(hypo),"adja;"+str(adj),"angle"+ str(y))


    drawer.pendown()
    drawer.left(y)
    dotter.hideturtle()
    drawer.forward(hypo)
    print(drawer.xcor(),drawer.ycor(),y)


    dotter.pencolor("purple")
    dotter.goto(drawer.xcor(),drawer.ycor())
    dotter.dot(10)
    dotter.penup()
    q1[y]=dotter.xcor()
    print(q1)

    drawer.left(-(y+90))
    drawer.forward(op)
    drawer.right(90)
    drawer.forward(adj)
    drawer.right(180)
    drawer.penup()

dotter.goto(300,300)
keylist = list(q1.keys())
for i in range (len(keylist)):
    dotter.goto(keylist[i]+300,q1.pop(keylist[i])+300)
    dotter.pendown()
    dotter.dot(10)
dotter.penup()
drawer.left(180)
for j in range (times):
    print(j)
    adj=random.randint(0,250)
    op= hypo**2-adj**2
    op=math.sqrt(op)
    x= math.asin(op/hypo)
    y= (x*180)/math.pi
    print("opo:"+str(op),"hype;"+str(hypo),"adja;"+str(adj),"angle"+ str(y))




    drawer.pendown()
    drawer.right(y)
    dotter.hideturtle()
    drawer.forward(hypo)
    print(drawer.xcor(),drawer.ycor(),180-y)

    dotter.pencolor("purple")
    dotter.goto(drawer.xcor(),drawer.ycor())
    dotter.dot(10)
    dotter.penup()
    q2[y]=dotter.xcor()
    print(q2)

    drawer.right(-(y+90))
    drawer.forward(op)
    drawer.left(90)
    drawer.forward(adj)
    drawer.left(180)
    drawer.penup()

dotter.goto(300,300)
keylist = list(q2.keys())
for i in range (len(keylist)):
    dotter.goto(keylist[i]+300,q2.pop(keylist[i])+300)
    dotter.pendown()
    dotter.dot(10)
dotter.penup()

drawer.left(180)
for k in range (times):
    print(k)
    adj=random.randint(0,250)
    op= hypo**2-adj**2
    op=math.sqrt(op)
    x= math.asin(op/hypo)
    y= (x*180)/math.pi
    print("opo:"+str(op),"hype;"+str(hypo),"adja;"+str(adj),"angle"+ str(y))




    drawer.pendown()
    drawer.right(y)
    dotter.hideturtle()
    drawer.forward(hypo)
    print(drawer.xcor(),drawer.ycor(),180-y)

    dotter.pencolor("purple")
    dotter.goto(drawer.xcor(),drawer.ycor())
    dotter.dot(10)
    dotter.penup()

    drawer.right(-(y+90))
    drawer.forward(op)
    drawer.left(90)
    drawer.forward(adj)
    drawer.left(180)
    drawer.penup()


drawer.left(180)
for k in range (times):
    print(k)
    adj=random.randint(0,250)
    op= hypo**2-adj**2
    op=math.sqrt(op)
    x= math.asin(op/hypo)
    y= (x*180)/math.pi
    print("opo:"+str(op),"hype;"+str(hypo),"adja;"+str(adj),"angle"+ str(y))




    drawer.pendown()
    drawer.left(y)
    dotter.hideturtle()
    drawer.forward(hypo)
    print(drawer.xcor(),drawer.ycor(),180-y)

    dotter.pencolor("purple")
    dotter.goto(drawer.xcor(),drawer.ycor())
    dotter.dot(10)
    dotter.penup()

    drawer.left(-(y+90))
    drawer.forward(op)
    drawer.right(90)
    drawer.forward(adj)
    drawer.right(180)
    drawer.penup()
