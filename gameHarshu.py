import turtle, random
screen = turtle.Screen()
screen.register_shape("ship",((-10,-10),(0,-5),(10,-10),(0,10)))
screen.register_shape("rock1",((-20, -16),(-21, 0),(-20,18), \
                               (0,27),(17,15),(25,0),(16,-15),(0,-21)))
screen.register_shape("rock2",((-15, -10),(-16, 0),(-13,12), \
                               (0,19),(12,10),(20,0),(12,-10),(0,-13)))
screen.register_shape("rock3",((-10,-5),(-12,0),(-8,8),(0,13), \
                               (8,6),(14,0),(12,0),(8,-6),(0,-7)))

ship = turtle.Turtle()
ship.shape("ship")
ship.penup()
ship.speed(0)
ship.color("green")
asteroids = []
for i in range(10) :
    a = turtle.Turtle()
    a.penup()
    a.speed(0)
    a.shape("rock" + str(random.randint(1,3)))
    a.goto(random.randint(-200,200),random.randint(-200,200))
    asteroids.append(a)
def right() :
    if(collision_detected(ship)):
        ship.hideturtle()
    ship.right(10)


def left() :
    if(collision_detected(ship)):
        ship.hideturtle()
    ship.left(10)

def forward() :
    if(collision_detected(ship)):
        ship.hideturtle()
    ship.forward(5)

def collision_detected(ship):
    for i in range(10) :
      if(ship.distance(asteroids[i]) < 30):
          return True
    return False

def getTheIndexOfAsteroidThatisHit(ammo):
    for i in range(10) :
      if(ammo.distance(asteroids[i]) < 30):
          return i
    return -1

def fire():
    print("Fire in the hole")



screen.onkey(right, "Right")
screen.onkey(left, "Left")
screen.onkey(forward, "Up")
screen.onkey(fire, "Tab")
screen.listen()
