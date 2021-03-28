# Day 6 : Hurdle 1 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(6):
    jump()

# Day 6 : Hurdle 2 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():    
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump()    

# Day 6 : Hurdle 3 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():    
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    elif front_is_clear():
        move()
        

# Day 6 : Hurdle 4 
def turn_right():
    turn_left()
    turn_left()
    turn_left()
        
while not at_goal():
    if wall_in_front():
        if right_is_clear(): 
            turn_right()
        else:
            turn_left()
            if wall_in_front():
                turn_left()                
    elif right_is_clear(): 
        turn_right()
    move()

# Day 6 : maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()
        
while not at_goal():
    if front_is_clear():
        move()
    else:
        if wall_on_right():
            turn_left()
        else:
            turn_right()