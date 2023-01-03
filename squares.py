import turtle as t

t.pensize(5)


def make_square(l, prev_l, j):
    if j == 7:
        return
    for i in range(4):
        t.forward(l)
        t.left(90)
    t.circle(l, 90)
    new_l = l + prev_l
    make_square(new_l, l, j + 1)


start_pos = t.Vec2D(400.00, -400.00)
t.penup()
t.setpos(start_pos)
t.pendown()
make_square(100, 0, 0)

t.done()
