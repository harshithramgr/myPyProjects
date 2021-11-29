import random
import turtle

from playsound import playsound

screen = turtle.Screen()
screen.bgcolor("black")
screen.register_shape("ship", ((-10, -10), (0, -5), (10, -10), (0, 10)))
screen.register_shape("rock1", ((-20, -16), (-21, 0), (-20, 18), \
                                (0, 27), (17, 15), (25, 0), (16, -15), (0, -21)))
screen.register_shape("rock2", ((-15, -10), (-16, 0), (-13, 12), \
                                (0, 19), (12, 10), (20, 0), (12, -10), (0, -13)))
screen.register_shape("rock3", ((-10, -5), (-12, 0), (-8, 8), (0, 13), \
                                (8, 6), (14, 0), (12, 0), (8, -6), (0, -7)))

ship = turtle.Turtle()
ship.shape("ship")
ship.penup()
ship.speed(0)
ship.color("green")
asteroids = []
bombExploded = False
global score
score = 0

points = turtle.Turtle()

for i in range(30):
    a = turtle.Turtle()
    a.penup()
    a.speed(0)
    a.shape("rock" + str(random.randint(1, 3)))
    a.goto(random.randint(-200, 200), random.randint(-200, 200))
    a.color("purple")
    asteroids.append(a)

for i in range(3):
    a.goto(random.randint(-200, 200), random.randint(-200, 200))


def bye(color):
    turtle.penup()
    turtle.hideturtle()
    turtle.color(color)
    style = ('Arial', 100, 'bold')
    turtle.setpos(0, 300)
    turtle.write('GAME OVER', font=style, align='center')


def right():
    if (collision_detected(ship)):
        ship.hideturtle()
        bomb()
        for i in range(10):
            bye('black')
            bye('green')
            bye('red')
            bye('white')
    ship.right(10)


def bomb():
    global bombExploded
    # print("value of bombExploded is"+str(bombExploded))
    if not bombExploded:
        bombExploded = True;
        playsound('sounds/explosion-trim.mp3')


def bomb2():
    playsound('sounds/explosion-trim.mp3')


def left():
    if (collision_detected(ship)):
        ship.hideturtle()
        bomb()
        for i in range(10):
            bye('black')
            bye('green')
            bye('red')
            bye('white')
    ship.left(10)


def forward():
    if (collision_detected(ship)):
        ship.hideturtle()
        bomb()
        for i in range(10):
            bye('black')
            bye('green')
            bye('red')
            bye('white')

    ship.forward(5)


def collision_detected(ship):
    for i in range(30):
        if (asteroids[i].isvisible() and ship.distance(asteroids[i]) < 30):
            return True
    return False


def getTheIndexOfAsteroidThatisHit(ammo):
    for i in range(30):
        if (asteroids[i].isvisible() and ammo.distance(asteroids[i]) < 30):
            return i
    return -1


def drawPoints(color):
    points.undo()
    points.penup()
    points.hideturtle()
    points.color(color)
    style = ('Arial', 100, 'bold')
    points.setpos(0, 300)
    points.write(score, font=style, align='center')


def fire():
    print("Fire in the hole")

    ammo = turtle.Turtle()
    ammo.shape('circle')
    ammo.penup()
    ammo.speed(0)
    ammo.color("red")
    ammo.setpos(ship.pos())
    ammo.seth(ship.heading())
    for i in range(30):
        ammo.forward(1)
        astroIndex = getTheIndexOfAsteroidThatisHit(ammo);
        if (astroIndex > 0):
            asteroids[astroIndex].hideturtle()
            ammo.hideturtle()
            bomb2()
            global score
            score = score + 10
            print(score)
            drawPoints('blue')
            break
    else:
        score = score - 5
        print(score)
        drawPoints('blue')
    ammo.hideturtle()


screen.onkey(right, "Right")
screen.onkey(left, "Left")
screen.onkey(forward, "Up")
screen.onkey(fire, "Tab")
screen.listen()
