import setup
import grid
import compute

import turtle


def convert_to_real(x, y, width):
    '''Converts grid coordinates to world coordinates.

    eg.
    convert_to_real(1,1, 50) -> (50, 50)
    '''

    real_x = x * width
    real_y = y * width

    return real_x, real_y


if __name__ == "__main__":
    # Setup the window, Hint: Setup module
    win = setup.setup("Example combined")

    # crate a turtle for drawing the grid
    grid_turtle = turtle.Turtle()
    grid_turtle.speed('fastest')

    # Attach to grid module
    grid.grid_turtle = grid_turtle

    # Call Part 2 code to create a grid
    grid.draw_grid(5, 5, 50)

    # Create the graph turtle

    graph_turtle = turtle.Turtle()
    compute.graph_turtle = graph_turtle

    # Call part 1 code to draw cylinders
    # Gen_Py_Cylinder_compute.draw_circle(50)
    # Gen_Py_Cylinder_compute.draw_cylinder(50, 100)
    x, y = convert_to_real(3, 3, 50)
    compute.cylinder_compute_draw(100, 100, x, y)

    # Run event loop
    win.mainloop()
