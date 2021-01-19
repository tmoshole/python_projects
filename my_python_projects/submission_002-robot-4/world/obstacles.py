import random
obstacles_list = []


def create_random_obstacles():
    """
    Creates a list of at least 10 obstacles with each coodinate in the 
    range of (-100, 100) for the x-coordinate and (-200, 200) for the 
    y-coordinate
    return: a list of obstacles
    """
    global obstacles_list
    num_of_obstacles = random.randint(1,10)
    for i in range(num_of_obstacles):
        x = random.randint(-100,101)
        y = random.randint(-200,201)
        obstacles_list.append((x,y))
    return obstacles_list


def is_position_blocked(x,y):
    """
    It checks if the new position is not in the blocked
    position.
    :param x: the new/proposed x position.
    :param y: the new/proposed y position.
    :return: True if the it falls in the blocked position.
    """

    obstacles_list = get_obstacles()
    
    for i in obstacles_list:
        if x in range(i[0],i[0] + 4) and y in range(i[1],i[1] + 4):
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
    obstacles_list = get_obstacles()
    
    for i in obstacles_list:
        if  x1 == x2 and x1 in range(i[0], i[0] + 4) and (i[1] in range(y1, y2) or i[1] in range(y1, y2,-1)):
            return True
        elif y1 == y2 and y1 in range(i[1], i[1]+4) and (i[0] in range(x1, x2) or i[0] in range(x1, x2, -1)):
            return True
    return False


def get_obstacles():
    """
    returns the list of randomly creared obsticles.
    """
    obstacles = obstacles_list
    return obstacles


