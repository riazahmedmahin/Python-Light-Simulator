# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @Mahin
import turtle

WIDTH = 820
HEIGHT = 140

wn = turtle.Screen()
wn.title("Python Light Simulator by @ Mahin")
wn.bgcolor("black")
wn.setup(WIDTH, HEIGHT)

color_codes = {
    "r": "red",
    "o": "orange",
    "y": "yellow",
    "g": "green",
    "b": "blue",
    "v": "purple",
    "w": "white",
    "p": "pink",
    " ": "black"
}

pen = turtle.Turtle()
pen.penup()
pen.color("black")
pen.shape("circle")


def draw_circle(x, y, pen):
    screen_x = -(WIDTH / 2.0) + 20 + x * 20
    screen_y = (HEIGHT / 2.0) - 20 - y * 20
    pen.goto(screen_x, screen_y)
    pen.stamp()


picture = [
    "    rrr o o yyy b  b www g   g",
    "    r r  oo  y  b  b w w gg  g",
    "    rr    o  y  bbbb w w g g g",
    "    r     o  y  b  b w w g  gg",
    "    r     o  y  b  b www g   g",
]

# Draw picture
for y in range(len(picture)):
    row = picture[y]
    for x in range(len(row)):
        color = picture[y][x]
        pen.color(color_codes[color])
        draw_circle(x, y, pen)

wn.mainloop()
