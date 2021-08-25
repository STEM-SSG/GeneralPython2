# Author        Alyk Skye
# Date          2021-07-17
# Revised       2021-07-19
# Variant       01.0
# Filename      Gen_Py_Turtle_Template_01-0.py
# Description   Sample Python Turtle graphics template for
#               QUT Student Sucess Group - General Python modules
# _______	________

# Import the required modules

import turtle           # Allows the use of the turtle


# User functions
# --------------

from compute import *


# Main program starts here
# ------------------------

# Control the size of the drawing space. Units are Pixels.
canvas_height = 600
canvas_width = 800

# Setup the canvas for the turtle drawing.
turtle.setup(canvas_width, canvas_height)

# Create the place to use the turtle for drawing.
turtle_window = turtle.Screen()

# Set the title at the top of the window
turtle_window.title("QUT General Python Example 1")

# User instruction or functions to make turtle move
cylinder_compute_prompt()

# Draw all the code to the screen
turtle_window.mainloop()

# Exit the program

