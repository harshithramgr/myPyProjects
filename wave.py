import turtle

screen=turtle.Screen()
dotter=turtle.Turtle()
axis = turtle.Turtle()
axis.penup()
axis.pencolor("blue")
axis.goto(0,0)
axis.pendown()
axis.forward(1000)
axis.right(180)
axis.forward(1000)

axis.right(90)
axis.forward(2000)

axis.hideturtle()

temp = {0:-3,0.16:-2, 0.32:-1, 0.48:0, 0.64:1 ,0.8:2, 0.96:3, 1.12:2, 1.28:1, 1.44:0, 1.6:-1, 1.76:-2, 1.92:-3}
keylist = list(temp.keys())
for i in range (len(keylist)):
    dotter.goto(keylist[i]*100,temp.pop(keylist[i])*100)
    dotter.dot(5)
print(keylist)
temp.pop(0)
for j in range (len(keylist)):
    dotter.goto(keylist[j]*200,temp.pop(keylist[j])*200)
    dotter.dot(5)
