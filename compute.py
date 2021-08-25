# Author        Alyk Skye
# Date          2021-07-31
# Revised       2021-08-03
# Variant       01.0
# Filename      Gen_Py_Turtle_
# Description   Sample Python Turtle graphics 
#               module to show operation of functions and turtle graphics            
# _______	________

# User option variables
# ---- ------ ---------

colour_circle = "yellow"
colour_cylinder = "red"


# Import the required modules
import turtle           # Allows the use of the turtle
from math import pi


# annotate the drawing

# Entry point to this collection of demostration functions
def cylinder_compute_prompt():

    graph_create_turtle()   # Create our turtle

    annotate_user_help()    # Put user help on the canvas

    # Prompt the user for the diameter, then draw and annotate 
    circle_diameter = user_input_int("Enter Cylinder Diameter")
    # print ("User typed Diameter = " + str(circle_diameter))
    draw_circle(circle_diameter)
    annotate_circle(circle_diameter)

    # Prompt the user for the length, then draw and annotate
    cylinder_length = user_input_int("Enter Cylinder Length")
    # print ("User typed Length   = " + str(cylinder_length))
    draw_cylinder(circle_diameter, cylinder_length)
    annotate_cylinder(circle_diameter, cylinder_length)

    # Compute the area and volume, then annotate drawing with details
    circle_area, cylinder_volume = cylinder_vol_calc(circle_diameter, cylinder_length)
    annotate_calulation(circle_diameter, circle_area, cylinder_length, cylinder_volume)
    
# Anternate entry point to this collection of demostration functions without prompting
def cylinder_compute_draw(circle_diameter, cylinder_length, circle_org_x = 0, circle_org_y = 0):

    graph_create_turtle()

    draw_circle(circle_diameter)
    annotate_circle(circle_diameter)

    # Draw and annotate the circle
    draw_cylinder(circle_diameter, cylinder_length)
    annotate_cylinder(circle_diameter, cylinder_length)

    # Compute the area and volume, then annotate drawing with details
    circle_area, cylinder_volume = cylinder_vol_calc(circle_diameter, cylinder_length)
    annotate_calulation(circle_diameter, circle_area, cylinder_length, cylinder_volume)


    
# Instansiate the turle ready to do the drawings on the canvas
def graph_create_turtle(): 
    global graph_turtle
    
    # Create the graph turtle
    graph_turtle = turtle.Turtle()    
    graph_turtle.shape("circle")    # Set turtle shape
    graph_turtle.color("purple")    # Set turtle colour
    graph_turtle.hideturtle()       # Make turtle invisible


# Prompt the user with pop-up dialogue box
def user_input_int(promt_text):
    user_text = turtle.textinput("User number input", promt_text)
    user_integer = int(user_text)
    
    return(user_integer)


# Draw the circle of given diameter with optional start point
def draw_circle(circle_diameter, circle_org_x = 0, circle_org_y = 0):
    # Compute the radius from the diameter
    circle_radius = compute_circle_radius(circle_diameter)

    graph_turtle.penup()
    # Position the centre of the circle
    graph_turtle.goto(circle_org_x, circle_org_y)

    # Perform the steps to draw a circle at the selected place
    graph_turtle.color(colour_circle)
    graph_turtle.begin_fill()
    graph_turtle.setheading(0)
    graph_turtle.forward(circle_radius)
    graph_turtle.left(90)
    graph_turtle.pendown()
    graph_turtle.begin_fill()
    graph_turtle.circle(circle_radius)
    graph_turtle.end_fill()
    

# Draw the cylinder of given length with optional start point
def draw_cylinder(circle_diameter, cylinder_length, circle_org_x = 0, circle_org_y = 0):
    # Compute the radius from the diameter
    circle_radius = compute_circle_radius(circle_diameter)

    # Position the centre of the circle
    graph_turtle.goto(circle_org_x, circle_org_y)

    # Performs the steps to draw the cylinder below the circle
    graph_turtle.color(colour_cylinder)
    graph_turtle.penup()
    graph_turtle.begin_fill()
    graph_turtle.setheading(90)
    graph_turtle.forward(circle_radius)
    graph_turtle.right(90)
    graph_turtle.pendown()
    graph_turtle.begin_fill()
    graph_turtle.forward(cylinder_length)
    graph_turtle.right(90)
    graph_turtle.forward(circle_diameter)
    graph_turtle.right(90)
    graph_turtle.forward(cylinder_length)
    graph_turtle.end_fill()
    graph_turtle.penup()


# Calculate the raduis of the circle from the given diameter
def compute_circle_radius(circle_diameter):

    # Compute the radius from the diameter
    circle_radius = circle_diameter // 2

    return(circle_radius)


# Write text to help user in interactive mode
def annotate_user_help():
    write_help_column = -350        # Value of X
    write_help_row = -250           # Value of Y
    writing_hight = 20              # Spacing for words

    # Heading text
    graph_turtle.penup()
    graph_turtle.color("Black")
    graph_turtle.goto(write_help_column, write_help_row)
    annotation = "Recommended sizes for Circle and Length are: "
    graph_turtle.write(annotation, align = 'left', font = ("Times", 14, 'bold'))
    
    # Size txt
    write_help_row -= writing_hight
    graph_turtle.goto(write_help_column, write_help_row)
    annotation = "Min 50 units and max 350 units"
    graph_turtle.write(annotation, align = 'left', font = ("Times", 14, 'normal'))
    


# Display the computed values of the area and volume
def annotate_calulation(circle_diameter, circle_area, cylinder_length, cylinder_volume):

    writing_start_column = -300     # Value of X
    writing_start_row = 230         # Value of Y
    writing_hight = 30              # Spacing for words

    # Heading text
    graph_turtle.color("Blue")
    graph_turtle.goto(writing_start_column, writing_start_row)
    annotation = "Display of area of circle and volume of cylinder "
    graph_turtle.write(annotation, align = 'left', font = ("Courier", 16, 'bold'))

    # Circle text
    writing_start_row -= writing_hight
    graph_turtle.goto(writing_start_column, writing_start_row)
    annotation = "Circle Diameter = " + str(circle_diameter) 
    graph_turtle.write(annotation, align = 'left', font = ("Courier", 16, 'normal'))

    writing_start_row -= writing_hight
    graph_turtle.goto(writing_start_column, writing_start_row)
    annotation = "           Area = " + str(round(circle_area, 2)) + " Units Squared."
    graph_turtle.write(annotation, align = 'left', font = ("Courier", 16, 'normal'))

    # Cylinder text
    writing_start_row -= writing_hight
    graph_turtle.goto(writing_start_column, writing_start_row)
    annotation = "Cylinder Length = " + str(cylinder_length)
    graph_turtle.write(annotation, align = 'left', font = ("Courier", 16, 'normal'))

    writing_start_row -= writing_hight
    graph_turtle.goto(writing_start_column, writing_start_row)
    annotation = "         Volume = " + str(round(cylinder_volume, 2)) + " Units Cubed."
    graph_turtle.write(annotation, align = 'left', font = ("Courier", 16, 'normal'))


# Draw dimension lines on the circle
def annotate_circle(circle_diameter, circle_org_x = 0, circle_org_y = 0):

    annotate_line_length = 100
    arrow_size = 12
    
    # Compute the radius from the diameter
    circle_radius = compute_circle_radius(circle_diameter)

    # determine right end of the dimension lines (x value)
    dim_line_right = circle_org_x - circle_radius

    # determine hight of top line (y value)
    dim_line_top = circle_org_y + circle_radius
    dim_line_bot = circle_org_y - circle_radius

    # Change the pen colour
    graph_turtle.color("Black")

    # Plot top dimension line
    graph_turtle.penup()
    graph_turtle.goto(dim_line_right, dim_line_top)
    graph_turtle.pendown()
    graph_turtle.setheading(180)
    graph_turtle.forward(annotate_line_length)
    graph_turtle.penup()
    
    # Plot bottom dimension line
    graph_turtle.goto(dim_line_right, dim_line_bot)
    graph_turtle.pendown()
    graph_turtle.setheading(180)
    graph_turtle.forward(annotate_line_length)
    graph_turtle.penup()

    # Configure and position to draw value line 
    graph_turtle.shape("triangle")
    graph_turtle.pensize(2)
    graph_turtle.setheading(0)
    graph_turtle.forward(annotate_line_length // 4)

    # Lower arrow point
    graph_turtle.pendown()
    graph_turtle.setheading(270)
    graph_turtle.forward(-arrow_size)
    graph_turtle.stamp()
    graph_turtle.setheading(90)
    graph_turtle.forward(circle_diameter // 3)
    graph_turtle.penup()

    graph_turtle.color("Blue")
    annotation = "Diameter = " + str(circle_diameter)
    graph_turtle.write(annotation, align = 'right', font = ("Courier", 16, 'bold'))
    graph_turtle.forward(circle_diameter // 3 - (arrow_size * 2))
    graph_turtle.color("Black")

    # Upper arrow point
    graph_turtle.pendown()
    graph_turtle.forward(circle_diameter // 3)
    graph_turtle.penup()
    graph_turtle.setheading(90)
    graph_turtle.stamp()

    
# Draw dimension lines on the cylinder
def annotate_cylinder(circle_diameter, cylinder_length, circle_org_x = 0, circle_org_y = 0):
    annotate_line_length = 100
    annotate_line_offset = 30
    arrow_size = 12
    
    # Compute the radius from the diameter
    circle_radius = compute_circle_radius(circle_diameter)

    # determine left end of the dimension lines (y value)
    dim_line_top = circle_org_y - circle_radius - annotate_line_offset

    # determine top point of both linex (x value)
    dim_line_left = circle_org_x
    dim_line_right = circle_org_x + cylinder_length

    # Change the pen colour
    graph_turtle.color("Black")

    # Plot left dimension line (under circle)
    graph_turtle.goto(dim_line_left, dim_line_top)
    graph_turtle.pendown()
    graph_turtle.setheading(270)
    graph_turtle.forward(annotate_line_length)
    graph_turtle.penup()

    # Plot right dimension line (end of cylinder)
    graph_turtle.goto(dim_line_right, dim_line_top)
    graph_turtle.pendown()
    graph_turtle.setheading(270)
    graph_turtle.forward(annotate_line_length)
    graph_turtle.penup()

    # Configure and position to draw value line 
    graph_turtle.shape("triangle")
    graph_turtle.pensize(2)
    graph_turtle.setheading(90)
    graph_turtle.forward(annotate_line_length // 4)

    # Right arrow point
    graph_turtle.pendown()
    graph_turtle.setheading(0)
    graph_turtle.forward(-arrow_size)
    graph_turtle.stamp()
    graph_turtle.setheading(180)
    graph_turtle.forward(cylinder_length // 3)
    graph_turtle.penup()

    graph_turtle.color("Blue")
    annotation = "Length = " + str(cylinder_length)
    graph_turtle.write(annotation, align = 'center', font = ("Courier", 16, 'bold'))
    graph_turtle.forward(cylinder_length // 3 - (arrow_size * 2))
    graph_turtle.color("Black")

    # Left arrow point
    graph_turtle.pendown()
    graph_turtle.forward(cylinder_length // 3)
    graph_turtle.penup()
    graph_turtle.setheading(180)
    graph_turtle.stamp()

 
# Compute the volume of a cylinder given ​diameter and length.​
def cylinder_vol_calc(diameter, length):
    cylinder_area = circle_area_calc(diameter)
    cylinder_volume = cylinder_area * length
    
    return(cylinder_area, cylinder_volume)

# Compute the area of a circle given its diameter​
def circle_area_calc(diameter):

    circle_radius = diameter / 2
    circle_area = pi * (circle_radius ** 2)

    return(circle_area)
