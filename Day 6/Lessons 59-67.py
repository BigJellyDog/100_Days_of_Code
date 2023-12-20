def turn_left():
    print("turned left")
    pass

def move():
    print("moved")
    pass

def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

def makesquare():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()

makesquare()