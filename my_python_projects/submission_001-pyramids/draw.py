

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    
    shape = ' '
    while shape == ' ':
        shape = input("Shape?: ")
        shape = shape.lower()
        if shape == 'pyramid' or shape == 'square' or shape == 'triangle' or shape == 'diamond' or shape=='x':
            break
        else:
            shape = ' '
            continue
    return shape


# TODO: Step 1 - get height (it must be int!)
def get_height():
    while True:
        height = input("Height?: ")
        if height.isdigit() and int(height) >0 and int(height) <80:
            break
        else:
            continue
    return int(height)

# TODO: Step 2
def draw_pyramid(height, outline):
    if outline == False:
        for j in range(height):
            for gaps in range(height-j-1):
                print(end=" ")
            for star in range(2*j +1):
                print("*",end="")
            print("")
    else:
        for j in range(height):
            for gaps in range(height-j-1):
                print(end=" ")
            for star in range(2*j +1):
                if star==0 or star==2*j or j==height-1:
                    print("*",end="")
                else:
                    print(end=" ")
            print()

# TODO: Step 3
def draw_square(height, outline):
    if outline == False:
      for i in range(height):
        print('*'*height)

    else:
        for i in range(height):
            for j in range(height):
                if i==0 or i==height-1 or j==0 or j==height-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print("")
    
    
# TODO: Step 4
def draw_triangle(height, outline):
    if outline == False:
        for i in range(1,height+1):
            print("*"*i)

    else: 
        for i in range(height):
            for j in range(i+1):
                if j==0 or i==(height-1) or i==j:
                     print("*",end="")
                else:
                    print(end=" ")
            print()


def draw_diamond(height, outline):
    for i in range(height):
        for j in range(height):
            if i+j==height-4 or i-j==height-4 or j-i==height-4 or i+j==height+2:
                print ("*",end="")
            else:
                print (end=" ")
        print()
def draw_x(height, outline):
    r=0
    t=4
    for i in range(height):
        for j in range(height):
            if i==r and j==t:
                print("*",end="")
                r=r+1
                t=t-1
            elif i==j:
                print("*",end="")
            else:
                print(end=" ")
        print()


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid":
        draw_pyramid(height, outline)
    elif shape == "square":
        draw_square(height, outline)
    elif shape == "triangle":
        draw_triangle(height, outline)
    elif shape == "diamond":
        draw_diamond(height, outline)
    elif shape == "x":
        draw_x(height, outline)



# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = ' '
    while outline == ' ':
        shape = input("Outline only? (y/N): ")
        shape = shape.lower()
        if shape == "y" or shape == "N":
            if shape == "y":
                return True
        elif shape == "n":
            return False
        else:
            shape == ' '
            continue


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

