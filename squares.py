# this program uses the turtle graphics package to draw a grid and a spiral through it.
# The length of every square in the grid has a length in the fibonacci sequence starting
# with 0 and 100. i e 0, 100, 100, 200, 300, 500 etc.

import turtle as t

t.pensize(5)


def make_square(l, prev_l, j):

    # base case
    if j == 7:
        return

    # draw square with side length l
    for i in range(4):
        t.forward(l)
        t.left(90)

    # draw spiral segment
    t.circle(l, 90)

    # increment length
    new_l = l + prev_l

    # recursive call with incremented length (new_ l) and index (j)
    make_square(new_l, l, j + 1)


start_pos = t.Vec2D(400.00, -400.00)
t.penup()

# set initial position of turtle
t.setpos(start_pos)

t.pendown()

# call function with initial square side length of 100 pixels
make_square(100, 0, 0)

t.done()
