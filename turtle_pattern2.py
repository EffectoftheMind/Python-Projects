import turtle

paint=turtle.Turtle()
paint.pencolor("orange")
paint.shape("turtle")

paint.forward(100)
paint.backward(50)
paint.right(90)
paint.forward(100)

paint.circle(-50, 100)

paint.done

tortoise=turtle.Turtle()
tortoise.pencolor("purple")
tortoise.shape("turtle")

tortoise.penup()
tortoise.forward(150)

tortoise.pendown()
tortoise.right(90)
tortoise.forward(150)
tortoise.left(90)
tortoise.forward(100)

tortoise.done

steve=turtle.Turtle()
steve.pencolor("pink")
steve.shape("turtle")

steve.penup()
steve.forward(300)

steve.pendown()
steve.forward(100)
steve.backward(50)
steve.right(90)
steve.forward(150)
