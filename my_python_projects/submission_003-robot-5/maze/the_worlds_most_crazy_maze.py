import random

obstacles_list = []

def create_random_obstacles():
    """
    Creates a maze
    """
    obstacles_list = []

    maze = [
    'xxx xxxxxxxxxxxxxxxxxxxxx',
    'x                       x',
    'x x  xxxxxxxxxxxxxxxxx  x',
    'x x  x         x     x  x',
    'x x  xxxxxxxx  xxxx  x  x',
    'x x  x         x  x  x  x',
    'x x  x   xxxxxxxxxxxxxxxx',
    'x                       x',
    'x                       x',
    'xxxxxxxxxxxxxxxxx  x    x',
    'x                  x    x',
    'x       xxxxxxxxxxxx    x',
    'xxxxxx  x               x',
    'x    x  x           xxxxx',
    'xxxxxx  x           x   x',
    'x       x   xxxxxxxxx   x',
    'x  xxxxxxx              x',
    'x                       x',
    'x  xxxxxxxxx   xxxxxxxxxx',
    'x          x   x        x',
    'xxxxxxxxx  x   xxxxxxxxxx',
    'x          x            x',
    'x  xxxxxx  x  xxxxxxxx  x',
    'x          x            x',
    'x  xxxxxxxxx  xxxxxxxxxxx',
    'x           S           x',
    'xxxxxxxxxxx   xxxxxxxxx x',
    'x          x          x x',
    'x          x xxxxxxx  x x',
    'x xxxxxxx  x          x x',
    'x x        x xxxxxxx  x x',
    'x x  xxxxxxx          x x',
    'x x           xxxxxxxxx x',
    'x xxxxxxxxxxxxx         x',
    'x               xxxxxxx x',
    'xxxxxxxxxxxxxxx         x',
    'x             x xxxxxxx x',
    'x xxxxxxxxxxx x         x',
    'x               xxxxxxx x',
    'xxx xxxxxxxxxxx         x',
    'x   x           xxxxxxx x',
    'xxx xxxxxxxxxxxxxxxxxxxxx',
    'x                       x',
    'xxx             xxxxxxxxx',
    'x   xxxxxxxxxxx x       x',
    'xxx           x x       x',
    'xxxxxxxxxxxxx x xxxxxxxxx',
    'x             x         x',
    'x xxxxxxxxxxxxxxxxxxxxx x',
    'x                       x',
    'xxxxxxxxxxxxxxxxxxxxx xxx',]

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            screen_x = -100 + (x*8)
            screen_y = 200 - (y*8)
            if maze[y][x] == "x":
                obstacles_list.append((screen_x,screen_y))
                # print(obstacles_list)
    return obstacles_list


def is_position_blocked(x,y):
    """
    It checks if the new position is not in the blocked
    position.
    :param x: the new/proposed x position.
    :param y: the new/proposed y position.
    :return: True if the it falls in the blocked position.
    """

    # obstacles_list = get_obstacles()

    print("in posi blocked")
    for i in obstacles_list:
        if x in range(i[0],i[0] + 8) and y in range(i[1],i[1] + 8):
            return True
    return False
    

def is_path_blocked(x1,y1, x2, y2):
    """
    It checks if the path which the turtle has to pass is not blocked.
    :para x1: first x-coordinate of the obstacles.
    :para x2: second x-coordinate of the obstacles.
    :para y1: first y-coordinate of the obstacles.
    :para y1: second y-coordinate of the obstacles.
    :return: True if the it falls in the blocked position.
    """ 
    # obstacles_list = get_obstacles()
    print("in path blocked")
    
    for i in obstacles_list:
        if  x1 == x2 and x1 in range(i[0], i[0] + 8) and (i[1] in range(y1, y2) or i[1] in range(y2, y1)):
            return True
        elif y1 == y2 and y1 in range(i[1], i[1]+8) and (i[0] in range(x1, x2) or i[0] in range(x2, x1)):
            return True
    return False


def get_obstacles():
    """
    returns the list of randomly creared obsticles.
    """
    obstacles = create_random_obstacles()
    return obstacles