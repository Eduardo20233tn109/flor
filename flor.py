from turtle import *

def tallo():
    speed(40)
    bgcolor("black")
    penup()
    goto(0, -100)
    pendown()
    color("green")
    begin_fill()
    right(90)
    forward(400)
    left(90)
    forward(20)
    left(90)
    forward(400)
    left(90)
    forward(20)
    end_fill()

def dibujar():
    m = 0
    penup()
    goto(0, 0)
    pendown()
    for i in range(16):
        for j in range(18):
            color("yellow")
            m += 0.005
            right(90)
            circle(150 - j * 6, 90)
            left(90)
            circle(150 - j * 6, 90)
            right(180)
        circle(40, 24)

def centro():
    penup()
    goto(-20, 0)
    pendown()
    color("#884513")
    begin_fill()
    circle(44)
    end_fill()

tallo()
dibujar()
centro()

done()
from turtle import *

def tallo():
    speed(40)
    bgcolor("black")
    penup()
    goto(0, -100)
    pendown()
    color("green")
    begin_fill()
    right(90)
    forward(400)
    left(90)
    forward(20)
    left(90)
    forward(400)
    left(90)
    forward(20)
    end_fill()

def dibujar():
    m = 0
    penup()
    goto(0, 0)
    pendown()
    for i in range(16):
        for j in range(18):
            color("yellow")
            m += 0.005
            right(90)
            circle(150 - j * 6, 90)
            left(90)
            circle(150 - j * 6, 90)
            right(180)
        circle(40, 24)

def centro():
    penup()
    goto(-20, 0)
    pendown()
    color("#884513")
    begin_fill()
    circle(44)
    end_fill()

tallo()
dibujar()
centro()

done()
