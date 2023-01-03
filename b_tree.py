import turtle as t
from math import acos, degrees

t.screensize(10000, 10000, "white")
t.pencolor("black")
t.pensize(5)
t.setheading(-90)
t.penup()
t.speed(0)


def make_tree(pos, h):
    if h == 0:
        return
    l = (75**2 + (2**h * 10 / 2)**2)**0.5
    angle = degrees(acos(75 / l))
    t.setpos(pos)
    t.seth(-90)
    t.left(angle / 2)
    t.pendown()
    t.forward(l)
    t.dot(10, "black")
    right_pos = t.pos()
    t.back(l)
    t.right(angle)
    t.forward(l)
    t.dot(10, "black")
    left_pos = t.pos()
    t.penup()
    make_tree(right_pos, h - 1)
    make_tree(left_pos, h - 1)


h = int(input("Select height: "))
origin = t.Vec2D(0.00, h * 100.00)
t.setpos(origin)
t.pendown()
t.dot(10)
t.penup()

make_tree(origin, h)

t.mainloop()
