from turtle import Turtle, Screen
from random import randrange, choice
import colorgram


def getTurtle():
    t = Turtle()
    t.shape("turtle")
    return t


def ch1():
    t = getTurtle()
    t.color("red")
    distance = 100
    angle = 90
    for _ in range(4):
        t.forward(distance)
        t.right(angle)


def ch2():
    t = getTurtle()
    t.color("green")
    step = 20
    for i in range(step):
        t.forward(10)
        if i % 2 == 0:
            t.penup()
        else:
            t.pendown()


def ch3():
    t = getTurtle()
    distance = 100
    for i in range(3, 11):
        t.pencolor(randomColor())
        angle = 360 / i
        for _ in range(i):
            t.forward(distance)
            t.right(angle)


def ch4():
    t = getTurtle()
    t.pensize(10)
    t.speed("fastest")
    distance = 50
    for _ in range(100):
        t.pencolor(randomColor())
        angle = randrange(360)
        t.forward(distance)
        t.right(angle)


def ch5():
    t = getTurtle()
    t.speed("fastest")
    radius = 100
    angle = 5
    for _ in range(int(360 / angle)):
        t.pencolor(randomColor())
        t.circle(radius)
        t.right(angle)


def randomColor():
    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    return (r, g, b)


def run():
    # colors = colorgram.extract("day18/image.jpg", 30)
    # drawColors = []
    # for c in colors:
    #     drawColors.append((c.rgb.r, c.rgb.g, c.rgb.b))
    # print(drawColors)
    drawColors = [
        (229, 228, 226),
        (225, 223, 224),
        (199, 175, 117),
        (124, 36, 24),
        (210, 221, 213),
        (168, 106, 57),
        (222, 224, 227),
        (186, 158, 53),
        (6, 57, 83),
        (109, 67, 85),
        (113, 161, 175),
        (22, 122, 174),
        (64, 153, 138),
        (39, 36, 36),
        (76, 40, 48),
        (9, 67, 47),
        (90, 141, 53),
        (181, 96, 79),
        (132, 40, 42),
        (210, 200, 151),
        (141, 171, 155),
        (179, 201, 186),
        (172, 153, 159),
        (212, 183, 177),
        (176, 198, 203),
        (150, 115, 120),
        (202, 185, 190),
        (40, 72, 82),
        (46, 73, 62),
        (47, 66, 82),
    ]
    t = getTurtle()
    t.hideturtle()
    t.speed("fastest")
    for y in range(10):
        for x in range(10):
            t.penup()
            t.setposition((-400 + 80 * x, -400 + 80 * y))
            t.pendown()
            curColor = choice(drawColors)
            t.dot(40, curColor)
            # t.pencolor(curColor)
            # t.fillcolor(curColor)
            # t.begin_fill()
            # t.circle(20)
            # t.end_fill()


def main():
    screen = Screen()
    screen.colormode(255)
    run()
    screen.exitonclick()


main()
