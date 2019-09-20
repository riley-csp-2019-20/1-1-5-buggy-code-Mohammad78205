#   a115_ladybug.py
import turtle as trtl

# make ladybug legs
ladybug = trtl.Turtle()
w = 6
y = 60
z = 360 / w
ladybug.pensize(5)
n = 0
while (n < w):
  ladybug.goto(0,-35)
  ladybug.setheading(z*n)
  ladybug.forward(y)
  n = n + 1
ladybug.hideturtle()
# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55)
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
num_dots = 0
while (num_dots < 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
 
  ypos = xpos + -10
  xpos = xpos
  num_dots = num_dots + 1
 
 
ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()

