import turtle as t

t.bgcolor("white")
t.pencolor("green")
t.pensize(5)
t.seth(90)
t.penup()
t.setpos(0.00, -400.00)
t.speed(0)
t.pendown()


def make_tree(l):
    if l < 20:
        t.pencolor("red")
        t.dot(20)
        t.pencolor("green")
        return
    t.forward(l)
    t.left(30)
    make_tree(l * 0.6)
    t.right(60)
    make_tree(l * 0.6)
    t.left(30)
    t.back(l)


make_tree(400)

t.mainloop()
