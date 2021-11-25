import math,turtle


op=input ("Please enter the opposite::")
adj=input ("Please enter the adjacent::")
hypo= input ("Please enter the hypotenuse::")

if hypo=="":
    dia= int(op)**2+int(adj)**2
    hypo = math.sqrt(dia)
    print("hypotenuse is " +str(hypo))

if op=="":
    oppo= int(hypo)**2-int(adj)**2
    op=math.sqrt(oppo)
    print("opposite is " +str(op))

if adj=="":
    adja=int(hypo)**2-int(op)**2
    adj=math.sqrt(adja)
    print("adjacent is " +str(adj))

x= math.asin(int(op)/int(hypo))
y= (x*180)/math.pi + 90

screen=turtle.Screen()
drawer = turtle.Turtle()

drawer.forward(int(adj)) # draw base

drawer.left(90)
drawer.forward(int(op))

drawer.left(y)
drawer.forward(int(hypo))

turtle.done()
