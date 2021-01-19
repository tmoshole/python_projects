

# TODO: Decompose into functions
def move():
    """
    Def moving_shapes : Name descibes what we are trying to achieve with this code
    """
    move_square(10)
    move_rectangle()
    move_circle()
    square_dancing()
    crop_circles()


    """
    this fnction we are moving the square
    """
def move_square(size):
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")


    """
    this function we are moving the rectangle
    """
def move_rectangle():
    length = 20
    width = 10
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")


    """
    this function we are moving a circle
    """
def move_circle():
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")


    """
    this function we making the square dance
    """
def square_dancing():
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        length = 20
        degrees = 90
        size = 20
        print("* Move Forward "+str(length))
        move_square(size)

        
    """
    this fuction we are cropping the circles
    """
def crop_circles():
    print("Crop circles - 4 circles")
    length = 20
    degrees = 1
    for i in range(4):
        print("* Move Forward "+str(length))
        move_circle()


def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
