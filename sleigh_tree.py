import turtle
import random
import math


# ---------- SETUP ----------
screen = turtle.Screen()
screen.title("Sleigh-the-Code 2.0")
screen.bgcolor("#87CEEB")        # soft sky blue

# Common settings
def setup_turtle(t, speed=0):
    t.speed(speed)
    t.penup()
    t.hideturtle()

# ---------- TREE ----------
tree = turtle.Turtle()
setup_turtle(tree)

# Tree trunk
tree.goto(-15, -150)
tree.color("#8B4513")
tree.pendown()
tree.begin_fill()
for _ in range(2):
    tree.forward(30)
    tree.left(90)
    tree.forward(40)
    tree.left(90)
tree.end_fill()
tree.penup()

# Triangular layers (aligned)
tree.color("#0B9B34")
base_y = -110           # bottom of lowest triangle
widths = [160, 120, 80] # bottom → top
heights = [50, 50, 50]

for w, h in zip(widths, heights):
    half = w / 2
    tree.goto(-half, base_y)
    tree.pendown()
    tree.begin_fill()
    tree.goto(0, base_y + h)
    tree.goto(half, base_y)
    tree.goto(-half, base_y)
    tree.end_fill()
    tree.penup()
    base_y += 30        # move up for next layer

top_y = base_y + 20     # top center of tree

# Star exactly on top
star = turtle.Turtle()
setup_turtle(star)
star.color("#FFD700")
star.goto(-12, top_y)
star.setheading(0)
star.pendown()
star.begin_fill()
for _ in range(5):
    star.forward(25)
    star.right(144)
star.end_fill()
star.penup()

# ---------- ORNAMENTS (match layers) ----------
orn = turtle.Turtle()
setup_turtle(orn)
colors = ["#FF4B4B", "#FFD700", "#1E90FF", "#FF69B4", "#ADFF2F"]

# y positions sit clearly inside each triangle
orn_positions = [
    # bottom layer (inside between -110 and -60)
    (-60, -95), (-30, -90), (0, -88), (30, -90), (60, -95),
    # middle layer (inside between -80 and -30)
    (-40, -65), (-15, -60), (15, -60), (40, -65),
    # top layer (inside between -50 and 0)
    (-25, -30), (0, -28), (25, -30)
]

for i, (x, y) in enumerate(orn_positions):
    orn.goto(x, y)
    orn.color(colors[i % len(colors)])
    orn.pendown()
    orn.begin_fill()
    orn.circle(5)
    orn.end_fill()
    orn.penup()

# ---------- GARLAND (follow layer widths) ----------
gar = turtle.Turtle()
setup_turtle(gar)
gar.color("#FFD700")
gar.pensize(3)

def draw_garland(y, width):
    left = -width / 2
    right = width / 2
    gar.goto(left, y)
    gar.pendown()
    steps = 20
    amp = 5
    for i in range(steps + 1):
        t = i / steps
        x = left + t * width
        offset = amp * math.sin(t * math.pi * 2)
        gar.goto(x, y + offset)
    gar.penup()

# y values chosen to sit clearly on each layer
draw_garland(-95, 150)   # bottom triangle
draw_garland(-65, 110)   # middle triangle
draw_garland(-35,  80)   # top triangle


# ---------- GIFTS ----------
gift = turtle.Turtle()
setup_turtle(gift)
gift_colors = ["#FF3030", "#32CD32", "#1E90FF"]

start_x = -70
for i in range(3):
    x = start_x + i * 45
    gift.goto(x, -140)
    gift.color(gift_colors[i], gift_colors[i])
    gift.pendown()
    gift.begin_fill()
    for _ in range(2):
        gift.forward(35)
        gift.left(90)
        gift.forward(25)
        gift.left(90)
    gift.end_fill()
    gift.penup()
    # ribbon
    gift.color("#FFD700")
    gift.pensize(2)
    gift.goto(x + 17.5, -140)
    gift.setheading(90)
    gift.pendown()
    gift.forward(25)
    gift.penup()
    gift.goto(x, -127)
    gift.setheading(0)
    gift.pendown()
    gift.forward(35)
    gift.penup()
    gift.pensize(1)

# ---------- SLEIGH ----------
sleigh = turtle.Turtle()
sleigh.hideturtle()
sleigh.speed(0)
sleigh.penup()

# body
sleigh.color("#FF0000")
sleigh.goto(-110, -165)
sleigh.pendown()
sleigh.begin_fill()
for _ in range(2):
    sleigh.forward(120)
    sleigh.left(90)
    sleigh.forward(25)
    sleigh.left(90)
sleigh.end_fill()
sleigh.penup()

# runner
sleigh.color("#8B4513")
sleigh.pensize(4)
sleigh.goto(-110, -175)
sleigh.pendown()
sleigh.forward(120)
sleigh.penup()

# wheels / curls (use explicit coordinates, no x variable)
sleigh.color("#000000")
sleigh.pensize(1)

# back wheel
sleigh.goto(-90, -180)
sleigh.pendown()
sleigh.begin_fill()
sleigh.circle(7)
sleigh.end_fill()
sleigh.penup()

# front wheel
sleigh.goto(10, -180)
sleigh.pendown()
sleigh.begin_fill()
sleigh.circle(7)
sleigh.end_fill()
sleigh.penup()
