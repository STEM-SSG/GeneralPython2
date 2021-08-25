# Author        Calvin Johnson
# Date          2021-07-30
# Revised       2021-08-02
# Variant       01.0
# Filename      Gen_Py_Grid.py
# Description   Sample Python Turtle graphics template for
#               QUT Student Sucess Group - General Python modules
# _______	________

import turtle           # Allows the use of the turtle
import time             # Time delay functions


# User functions
# --------------


'''
draws a square at the given (x,y) coordinate, with the specified side width
'''
def draw_square(x, y, width):
	pass

'''
draws a grid centered at the origin (centre of screen),
with grid_width and grid_height being how many squares in the positive x and y direction,
and tile_width is the width of each grid square.

NOTE: also draws in the negative x and y direction, using same number of squares as is in positive x and y
'''
def draw_grid(grid_width, grid_height, tile_width):
    # use the preexisting grid_turtle variable
    global grid_turtle

    # draw grid, set outline colour
    grid_turtle.color("light grey")

    # loop through each grid square location and draw it
    for x in range(-grid_width, grid_width):
        for y in range(-grid_height, grid_height):
            # TODO: Call draw_square_vx function with correct parameters
            pass

    # draw axis
    grid_turtle.color("black")
    draw_axis(grid_width, grid_height, tile_width)

'''
draws the grid axis centered at the origin corresponding to
the grid given by grid_width, grid_height, and tile_width
(as seen in draw_grid())
'''
def draw_axis(grid_width, grid_height, tile_width):
    # use the preexisting grid_turtle variable
    global grid_turtle
    grid_turtle.penup()    

    # horizontal axis

    # go to left point of horizontal axis, and label it
    grid_turtle.goto(-grid_width * tile_width, 0)
    grid_turtle.write(str(-grid_width), align = 'center', font = ("times", 22, 'bold'))

    # move to right side of axis and trace path to draw the axis line
    grid_turtle.pendown()
    grid_turtle.setheading(0)
    grid_turtle.forward(2 * grid_width * tile_width)
    # label right side point on axis
    grid_turtle.write(str(grid_width), align = 'center', font = ("times", 22, 'bold'))
    # pen up so we don't draw extra line when moving to vertical axis
    grid_turtle.penup()

    # vertical axis

    # go to bottom point of vertical axis, and label it
    grid_turtle.goto(0, -grid_height * tile_width)

    # move to top of axis and trace path to draw the axis line
    grid_turtle.write(str(-grid_height), align = 'center', font = ("times", 22, 'bold'))
    grid_turtle.pendown()
    grid_turtle.setheading(90)
    grid_turtle.forward(2 * grid_width * tile_width)
    # label top point on axis
    grid_turtle.write(str(grid_height), align = 'center', font = ("times", 22, 'bold'))

    # pen up so we don't draw in the next function accidentally
    grid_turtle.penup()

'''
draws a point at the given (x,y) pair, scaled by the given tile_width
'''
def plot_point(x, y, tile_width, color, shape):
    # use the preexisting grid_turtle variable
    global grid_turtle
    
    # make sure pen is up
    grid_turtle.penup()

    # set colour and shape appropriately
    # TODO: Configure Turtle

    # go to correct grid point and stamp turtle
    # TODO: Draw point

# Main program starts here
# ------------------------
if __name__ == '__main__':
    from setup import setup
    turtle_window = setup("QUT General Python Example 1")

    # turn tracer off to draw grid instantly
    grid_turtle = turtle.Turtle()
    # change speed to draw faster when tracer is on
    grid_turtle.speed('fastest')

    # set grid width and height, and size of each grid square
    grid_width = 5
    grid_height = 5
    tile_width = 50

	# grid code goes here
	
    # Draw all the code to the screen
    turtle_window.mainloop()

# Exit the program