#   a115_buggy_image.py
import turtle as trtl

drawer = trtl.Turtle()
drawer.pensize(40)
drawer.circle(20)
legs = 8
leg_length = 70
leg_space = 360 / legs
drawer.pensize(5)
count = 0
while (count < legs):
  drawer.goto(0,20)
  drawer.setheading(leg_space*count)
  drawer.forward(leg_length)
  count = count + 1
drawer.hideturtle()
wn = trtl.Screen()
wn.mainloop()
