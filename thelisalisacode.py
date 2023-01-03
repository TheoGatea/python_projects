import turtle
import math

pen = turtle.Turtle()


def draw_i():
    pen.forward(60)
    pen.back(120)
    pen.forward(60)
    pen.left(90)
    pen.forward(160)
    pen.right(90)
    pen.back(60)
    pen.forward(120)


def draw_y():
    pen.left(45)
    pen.forward(220)
    pen.back(110)
    pen.left(90)
    pen.forward(110)


def draw_u():
    pen.left(90)
    pen.forward(60)
    pen.pendown()
    pen.forward(100)
    pen.right(180)
    pen.forward(100)
    pen.circle(60, 180)
    pen.forward(100)


def draw_L():
    pen.left(90)
    pen.forward(160)
    pen.back(160)
    pen.right(90)
    pen.forward(80)


def draw_s():
    pen.forward(30)
    pen.circle(40, 180)
    pen.circle(-40, 180)
    pen.forward(30)


def draw_a():
    l = 160 / math.cos(math.pi / 12)
    m = math.sqrt(l**2 - 160**2)
    pen.left(75)
    pen.forward(l)
    pen.right(150)
    pen.forward(l)
    pen.back(l / 2)
    pen.right(105)
    pen.forward(m)


def draw_heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    pen.circle(-57, 200)
    pen.left(120)
    pen.circle(-57, 200)
    pen.forward(112)
    pen.end_fill()


base_height_l1 = 100.00
base_height_l2 = -200.00

turtle.bgcolor("pink")
pen.pencolor("black")
pen.speed(0)
pen.penup()
pen.setpos(-450.00, base_height_l1)
pen.pendown()
pen.pensize(10)

draw_i()

pen.penup()
pen.right(90)
pen.forward(160)
pen.left(90)
pen.forward(200)
pen.pendown()

draw_heart()

pen.penup()
pen.left(140)
pen.forward(180)
pen.pendown()

draw_y()

pen.penup()
pen.back(220)
pen.right(135)
pen.forward(100)
pen.pendown()

# draw O
pen.circle(80)

pen.penup()
pen.forward(150)

draw_u()

pen.penup()
pen.right(90)
pen.setpos(-300.00, base_height_l2)
pen.pendown()

draw_L()

pen.penup()
pen.forward(120)
pen.pendown()

draw_i()

pen.penup()
pen.right(90)
pen.forward(160)
pen.left(90)
pen.forward(70)
pen.pendown()

draw_s()

pen.penup()
pen.right(90)
pen.forward(160)
pen.left(90)
pen.forward(70)
pen.pendown()

draw_a()

turtle.mainloop()
