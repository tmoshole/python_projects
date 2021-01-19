
def robot_start():
    """This is the entry function, do not change"""
    y = 0
    x = 0
    var = 1
    num = 0
    name = name_robot()
    scommand = game_commands(name,y,var,x,num)
    # help_command()
    # move_forward(name,scommand,y)
    #x = updating_x(scommand)
    
def name_robot():
    """Allowing the user to name the robot.
    """
    name = input("What do you want to name your robot? ")
    print(name+': Hello kiddo!')
    return name

def game_commands(name,y,var,x,num):
    """ giving the game commands"""

    while True:
        command = input(name+': What must I do next? ')
        scommand = command.split(' ') #used the split command to split the command input
     
        if scommand[0].lower() == 'off':
            print(name+': Shutting down..')
            break
        elif scommand[0].lower() == 'help':
            help_command()
        elif scommand[0].lower() == 'forward' : 
            y = updating_y(scommand,y,var,name,x)
            x = updating_x(scommand,x,var,name,y)
            print(f" > {name} now at position ({x},{y}).")

        elif scommand[0].lower()== 'back':
            y = updating_y(scommand,y,var,name,x)
            x = updating_x(scommand,x,var,name,y)
            print(f" > {name} now at position ({x},{y}).")
        elif scommand[0].lower() == 'right':
            var = turn_Right(scommand,var)
            print(' >', name,'turned right.')
            print(f" > {name} now at position ({x},{y}).")
        elif scommand[0].lower() == 'left':
            var = turn_left(scommand,var)
            print(' >', name,'turned left.')
            print(f" > {name} now at position ({x},{y}).")
        elif scommand[0].lower() == 'sprint':
            num = scommand[1]
            x, y = sprint(num,name,scommand,y,var,x)
            print(f" > {name} now at position ({x},{y}).")
        else:
            print(name+': Sorry, I did not understand', '\''+command+'\'.')
    return scommand       
def help_command():

    instructions = ["I can understand these commands:",
    "OFF  - Shut down robot",
    "HELP - provide information about commands",
    "FORWARD - move forward by specified number of steps, e.g. FORWARD 10",
    "BACK - move back by specified number of steps, e.g. back 20",
    "RIGHT - For the robot to turn right",
    "LEFT - For the robot to turn left",
    "SPRINT"]
    for x in instructions:
        print(x)

    return instructions

def move_forward(name,scommand,y,x):
    """
    the move forward function
    """

    return print(' >', name,'moved forward by', scommand[1],'steps.')


def move_back(name,scommand,y,x):
    """
    the move back function
    """

    return print(' >', name,'moved back by', scommand[1],'steps.')

def turn_Right(scommand,var):
    """funtion to turn right"""
    if var == 4:
        var = 1
    else:
        var +=1
    return var

def turn_left(scommand,var):
    """funtion to turn left"""
    if var == 1:
        var = 4
    else:
        var -=1
    return var

def sprint(num,name,scommand,y,var,x):
    """
    the sprint function
    """
    num = int(num)
    if num <= 1:
        print(' >', name,'moved forward by', num,'steps.')
        y = updating_y([scommand[0], num],y,var,name,x)
        x = updating_x([scommand[0], num],x,var,name,y) 
        return x,y
    else:
        print(' >', name,'moved forward by', num,'steps.')
        y = updating_y([scommand[0],num],y,var,name,x)
        x = updating_x([scommand[0], num],x,var,name,y)
        num -= 1
        return sprint(num,name,scommand,y,var,x)


def updating_y(scommand,y,var,name,x):
    """
    function to update y
    """
    y_update = int(scommand[1])

    if var == 1:
        if scommand[0].lower() == 'forward':
            if (y_update + y) > 200:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                y = y_update + y
        
                move_forward(name,scommand,y,x)

        elif scommand[0].lower() == 'sprint':
            if (y_update + y) > 200:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                y = y_update + y
                y_update -= 1

        elif scommand[0].lower() == 'back':
            if (y - y_update) < -200:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                y = y - y_update
                move_back(name,scommand,y,x)
                


    elif var == 3:
        if scommand[0].lower() == 'forward':
            if (y_update - y) < -200:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                y = y - y_update 
                move_forward(name,scommand,y,x)

        elif scommand[0].lower() == 'back':
            if (y + y_update) > 200:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                y = y + y_update
                move_back(name,scommand,y,x)
        elif scommand[0].lower() == 'sprint':
            if (y_update - y) < -200:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                y = y - y_update
                y_update -= 1


    return y

def updating_x(scommand,x,var,name,y):
    """
    function to update y
    """
    x_update = int(scommand[1])
    if var == 2:
        if scommand[0].lower() == 'forward':
            if (x_update + x) > 100:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                x = x_update + x
                move_forward(name,scommand,y,x)
        elif scommand[0].lower() == 'back':
            if (x - x_update) < -100:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                x = x - x_update
                move_back(name,scommand,y,x)

        elif scommand[0].lower() == 'sprint':
            if (x_update + x) > 100:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                x = x_update + x
                x_update -= 1

    elif var == 4:
        if scommand[0].lower() == 'forward':
            if (x - x_update) < -100:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                x = x - x_update
                move_forward(name,scommand,y,x)
        elif scommand[0].lower() == 'back':
            if (x_update + x) > 100:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                x = x + x_update
                move_back(name,scommand,y,x)
        elif scommand[0].lower() == 'sprint':
            if (x - x_update) < -100:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                x = x - x_update
                x_update -= 1
    
    return x


if __name__ == "__main__":
    robot_start()
