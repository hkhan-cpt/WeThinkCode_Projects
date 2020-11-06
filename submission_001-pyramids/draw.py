

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape_selection= input("Shape?: ").lower()
    
    
    while shape_selection !="pyramid" and shape_selection !="square" and  shape_selection !="triangle" and shape_selection!="rectangle" and shape_selection !="parallelogram" and  shape_selection !="diamond":
        shape_selection= input("Shape?: ").lower()
    return shape_selection
       

# TODO: Step 1 - get height (it must be int!)
def get_height():
    global height
    height= input("Height?: ")

    while height.isdigit()==False or int(height)>80:
        height= input("Height?: ")
    return int(height)


# TODO: Step 2
def draw_pyramid(height, outline):
    if (outline==True):
        for x in range(0, height):
            for y in range(0,height-x-1):
                print(" ", end="")
            for y in range(0, 2*x+1):
                if y==0 or y==2*x or x==height-1:
                    print("*", end ="")
                else:
                    print(end=" ")
            print()
        
    else:
        for x in range(0, height):
            for y in range(0,height-x-1):
                print(" ", end="")
            for y in range(0, 2*x+1):
                if y==0 or y==2*x or x==height-1:
                    print("*", end ="")
                else:
                    print(end="*")
            print()
        
    

# TODO: Step 3
def draw_square(height, outline):
    if (outline == True):
        for x in range(0, height):
            for y in range(0, height):
                if x==0 or x==height-1 or y==0 or y==height-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    else:
        for x in range(0, height):
            for y in range(0, height):
                if y<=x:
                    print("*", end="")
                else:
                    print("*", end="")
            print()


# TODO: Step 4
def draw_triangle(height, outline):
    if (outline==True):
        for x in range(0, height):
            for y in range(0, x+1):
                if x==y or x==height-1 or y==0:
                    print("*", end="")
                else:
                    print(end=" ")
            print()
    else:
        for x in range(0, height):
            for y in range(0, x+1):
                print("*", end="")
            print()

def draw_rectangle(height, outline):
    if (outline==True):
        length= 3*height
        for x in range(0, height):
            for y in range(0, length):
                if x==0 or x==height-1 or y==0 or y ==length-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        
    else:
        length= 3*height
        for x in range(0, height):
            for y in range(0, height):
                print(end="")
            for y in range(0, length):
                print("*", end="")
            print()

def draw_parallelogram(height, outline):
    if (outline==True):
        length=3*height
        for x in range(0, height):
            for y in range(0, height-x):
                print(end=" ")
            if x==0 or x==height-1:
                for y in range (0, length):
                    print("*", end="")
            else:
                for y in range (0, length):
                    if y==0 or y==length-1:
                        print("*", end="")
                    else:
                        print(end=" ")
            print()
         
    else:
        for x in range(0, height):
            for y in range(0, height-x):
                print(end=" ")
            for y in range (0, 3*height):
                print("*", end="")
            print()

def draw_diamond(height, outline):
    if (outline==True):
        for x in range(0, height):
            for y in range(0, height-x):
                print(" ", end="")
            for y in range(0, 2*x):
                if y==0 or y==2*x-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

        for x in range(height, 0, -1):
            for y in range(0, height-x):
                print(" ", end="")
            for y in range(0, 2*x):
                if y==0 or y==2*x-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    else:
        for x in range(0, height):
            for y in range(0, height-x):
                print(" ", end="")
            for y in range(0, 2*x):
                if y==0 or y==2*x-1:
                    print("*", end="")
                else:
                    print("*", end="")
            print()

        for x in range(height, 0, -1):
            for y in range(0, height-x):
                print(" ", end="")
            for y in range(0, 2*x):
                if y==0 or y==2*x-1:
                    print("*", end="")
                else:
                    print("*", end="")
            print()



# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape=="pyramid":
        draw_pyramid(height, outline)
    if shape=="square":
        draw_square(height, outline)
    if shape=="triangle":
        draw_triangle(height, outline)
    if shape=="rectangle":
        draw_rectangle(height, outline)
    if shape=="parallelogram":
        draw_parallelogram(height, outline)
    if shape=="diamond":
        draw_diamond(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline_option= input("Outline only (y/N): ")
    
    if outline_option== "y":
        return True
    else:
        return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

