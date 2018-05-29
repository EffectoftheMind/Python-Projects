import turtle
paint=turtle.Turtle()
paint.shape("turtle")
paint.speed('fastest')
paint.penup()
paint.right(90)
paint.forward(100)


def circles():
  paint.pencolor("Maroon")
  paint.right(90)
  paint.circle(50)
  paint.pencolor("plum")
  paint.circle(100)


paint.pendown()
circles()
circles()
circles()
circles()

