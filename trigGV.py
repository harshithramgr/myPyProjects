import random,turtle,math
screen=turtle.Screen()
drawer = turtle.Turtle()
dotter=turtle.Turtle()
axis = turtle.Turtle()
circleOrigin = 0
xplotOrigin = 350
yplotOrigin = -1000
hypo=250

# Draw Circle Axis
axis.pencolor("blue")
axis.goto(circleOrigin,circleOrigin)
axis.forward(hypo)
axis.left(180)
axis.forward(hypo*2)
axis.goto(0,0)
axis.left(90)
axis.forward(hypo)
axis.left(180)
axis.forward(hypo*2)
axis.hideturtle()
axis.penup()

# Draw Plot Axis
def plotAxis(plotOrigin,message):
    axis.goto(plotOrigin,0)
    axis.right(180)
    axis.pencolor("black")
    axis.pendown()
    axis.forward(hypo)
    axis.left(180)
    axis.forward(hypo*2)
    axis.goto(plotOrigin,0)

    axis.right(90)
    axis.forward(hypo*2)
    axis.hideturtle()
    axis.penup()
    axis.goto(plotOrigin,400)
    axis.write(message,font=("Verdana",15, "bold"))

plotAxis(xplotOrigin," X axis = Angle of Hypotnuse. Y Axis = X coordinate of the circle")
axis.left(90)
plotAxis(yplotOrigin," X axis = Angle of Hypotnuse. Y Axis = Y coordinate of the circle")


dotter.penup()
drawer.speed(0)


times=10
plotxdata={}
plotydata={}

def plot(plotdata,color,offset,plotOrigin):
    dotter.pencolor(color)
    dotter.goto(0,plotOrigin)
    keylist = list(plotdata.keys())
    for i in range (len(keylist)):
        dotter.goto((abs(offset-keylist[i])+plotOrigin),plotdata.pop(keylist[i]))
        dotter.pendown()
        dotter.penup()
        dotter.dot(2)
    dotter.penup()

def drawQ(qudrantNumber,color):
    for i in range (times):
        #print(i)
        adj=random.randint(0,250)
        op= hypo**2-adj**2
        op=math.sqrt(op)
        x= math.asin(op/hypo)
        y= (x*180)/math.pi
        ##print("opo:"+str(op),"hype;"+str(hypo),"adja;"+str(adj),"angle"+ str(y))
        drawer.pendown()
        if(qudrantNumber == 1 or qudrantNumber == 3):
            drawer.left(y)
        if(qudrantNumber == 2 or qudrantNumber == 4):
            drawer.right(y)
        dotter.hideturtle()
        drawer.forward(hypo)
        #print(drawer.xcor(),drawer.ycor(),y)

        dotter.pencolor(color)
        dotter.goto(drawer.xcor(),drawer.ycor())
        dotter.dot(10)
        dotter.penup()
        plotxdata[y]=drawer.xcor()
        plotydata[y]=drawer.ycor()
        #print(plotdata)

        if(qudrantNumber == 1 or qudrantNumber == 3):
            drawer.left(-(y+90))
        if(qudrantNumber == 2 or qudrantNumber == 4 ):
            drawer.right(-(y+90))

        drawer.forward(op)
        if(qudrantNumber == 1 or qudrantNumber == 3):
            drawer.right(90)
        if(qudrantNumber == 2 or qudrantNumber == 4):
            drawer.left(90)

        drawer.forward(adj)
        if(qudrantNumber == 1 or qudrantNumber == 3):
            drawer.right(180)
        if(qudrantNumber == 2 or qudrantNumber == 4):
            drawer.left(180)

        drawer.penup()

#Draw Q1
drawQ(1,"purple")
drawer.left(180)
#Plot for Q1
plot(plotxdata,"purple",0,xplotOrigin)
plot(plotydata,"purple",0,yplotOrigin)
plotxdata={}
plotydata={}

#Draw Q2
drawQ(2,"orange")
drawer.left(180)
#Plot for Q2
plot(plotxdata,"orange",180,xplotOrigin)
plot(plotydata,"orange",180,yplotOrigin)
plotydata={}
plotxdata={}

#Draw Q3
drawQ(4,"green")
drawer.left(180)
#Plot for Q2
plot(plotxdata,"green",360,xplotOrigin)
plot(plotydata,"green",360,yplotOrigin)
plotydata={}
plotxdata={}

#Draw Q4
drawQ(3,"brown")
drawer.left(180)
#Plot for Q2
plot(plotxdata,"brown",-180,xplotOrigin)
plot(plotydata,"brown",-180,yplotOrigin)
plotydata={}
plotxdata={}

dotter.goto(xplotOrigin,-300)
dotter.write("COSINE",font=("Verdana",15, "bold"))

dotter.goto(yplotOrigin,-300)
dotter.write("SINE",font=("Verdana",15, "bold"))
