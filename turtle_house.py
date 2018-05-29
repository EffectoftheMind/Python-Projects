import turtle

paint = turtle.Turtle()
paint.pencolor("#855826")
paint.fillcolor("#855826")
paint.speed("fastest")

paint.fill(True)
paint.left(90)
paint.forward(100)
paint.penup()
paint.right(90)
paint.forward(50)
paint.pendown()
paint.circle(50)
paint.left(180)
paint.forward(50)
paint.right(90)
paint.forward(50)
paint.fill(False)

paint.fill(True)
paint.right(90)
paint.forward(100)
paint.right(90)
paint.forward(150)
paint.right(90)
paint.forward(100)
paint.fill(False)

paint.pencolor("red")
paint.penup()
paint.right(90)
paint.forward(100)
paint.right(90)
paint.forward(90)
paint.right(90)
paint.dot(10, "black")

paint.forward(100)
paint.left(90)
paint.forward(10)

paint.fill(True)
paint.pencolor("#feffe8")
paint.fillcolor("#feffe8")
paint.pendown()

for i in range(4):
  paint.forward(600)
  paint.left(90)
  
paint.fill(False)

paint.forward(300)
paint.left(90)
paint.forward(50)
paint.pencolor("#24d63d")
paint.fillcolor("#24d63d")

paint.fill(True)
paint.left(90)
paint.forward(150)
paint.left(90)
paint.forward(25)
paint.left(90)
paint.forward(300)
paint.left(90)
paint.forward(25)
paint.left(90)
paint.forward(150)
paint.fill(False)
paint.forward(150)
paint.left(90)
paint.forward(25)

paint.pencolor("#9024d6")
paint.fillcolor("#05e1e8")
paint.fill(True)
paint.forward(25)
paint.left(90)
paint.forward(300)
paint.left(90)
paint.forward(25)
paint.left(90)
paint.forward(300)
paint.fill(False)

paint.penup()
paint.right(90)
paint.forward(12.5)
paint.right(90)
for x in range(4):
  paint.forward(20)
  paint.dot(5, "red")
  paint.forward(40)
  paint.dot(5, "red")
  
paint.forward(20)
paint.dot(5, "red")
paint.forward(40.5)
paint.left(90)
paint.forward(100)
paint.left(90)
paint.pencolor("#855826")
paint.pendown()
paint.pensize(10)

for i in range(4):
  paint.forward(300)
  paint.right(90)
  
paint.forward(150)
paint.fillcolor("#d0fffe")
paint.fill(True)

for i in range(4):
  paint.right(90)
  paint.forward(150)
paint.fill(False)

paint.right(90)
paint.fill(True)

for i in range(4):
  paint.forward(150)
  paint.left(90)
  
paint.fill(False)

paint.forward(150)
paint.fill(True)

for i in range(4):
  paint.forward(150)
  paint.right(90)
  
paint.fill(False)

paint.fill(True)

for i in range(4):
  paint.forward(150)
  paint.left(90)
  
paint.fill(False)

paint.forward(150)
paint.left(90)
paint.forward(150)
paint.right(180)
paint.penup()


paint.dot(20, "#d815ca")
paint.forward(43)
paint.dot(20, "#7d09bb")

paint.forward(43)
paint.dot(20, "#d815ca")

paint.forward(43)
paint.dot(20, "#7d09bb")

paint.forward(43)
paint.dot(20, "#d815ca")

paint.forward(43)
paint.dot(20, "#7d09bb")

paint.forward(43)
paint.dot(20, "#d815ca")

paint.forward(43)
paint.dot(20, "#7d09bb")

paint.forward(19)
paint.left(90)

paint.pencolor("#7d09bb")
paint.pendown()
paint.pensize(1)
paint.fillcolor("#7d09bb")
paint.fill(True)

def rectangles():
  paint.forward(40)
  paint.left(90)
  paint.forward(37)
  paint.left(90)
  paint.forward(40)

rectangles()
paint.fill(False)

def new_stripe():
  paint.penup()
  paint.right(90)
  paint.forward(6)
  paint.right(90)

new_stripe()
paint.pencolor("#d815ca")
paint.fillcolor("#d815ca")
paint.pendown()

paint.fill(True)
rectangles()
paint.fill(False)

new_stripe()
paint.pencolor("#7d09bb")
paint.fillcolor("#7d09bb")
paint.pendown()

paint.fill(True)
rectangles()
paint.fill(False)

new_stripe()
paint.pencolor("#d815ca")
paint.fillcolor("#d815ca")
paint.pendown()

paint.fill(True)
rectangles()
paint.fill(False)

new_stripe()
paint.pencolor("#7d09bb")
paint.fillcolor("#7d09bb")
paint.pendown()

paint.fill(True)
rectangles()
paint.fill(False)

new_stripe()
paint.pencolor("#d815ca")
paint.fillcolor("#d815ca")
paint.pendown()

paint.fill(True)
rectangles()
paint.fill(False)

new_stripe()
paint.pencolor("#7d09bb")
paint.fillcolor("#7d09bb")
paint.pendown()

paint.fill(True)
rectangles()
paint.fill(False)

new_stripe()
paint.pencolor("#d815ca")
paint.fillcolor("#d815ca")
paint.pendown()

paint.fill(True)
rectangles()
paint.fill(False)

paint.left(180)
paint.forward(40)

paint.right(90)
paint.penup()
paint.forward(37)

paint.pencolor("black")
paint.fillcolor("black")
paint.pendown()

def small_rectangles():
  paint.fill(True)
  paint.forward(5)
  paint.right(90)
  paint.forward(35)
  paint.right(90)
  paint.forward(5)
  paint.right(90)
  paint.forward(35)
  paint.fill(False)
  paint.penup()
  paint.right(90)
  paint.forward(43)
  paint.pendown()
  
for x in range(7):
  small_rectangles()
  
paint.penup()
paint.backward(400)
paint.right(90)
paint.forward(320)
paint.right(90)
paint.forward(71)
paint.right(90)

paint.pendown()
paint.color("#feffe8")
paint.fill(True)
paint.forward(10)
paint.left(27)
paint.forward(10)
paint.left(20)
paint.forward(20)
paint.right(54)
paint.forward(400)
paint.fill(False)

paint.penup()
paint.home()
paint.left(90)

paint.pendown()
paint.forward(600)
paint.right(90)
paint.forward(300)

paint.fill(True)
paint.right(90)
paint.forward(100)
paint.right(90)
paint.forward(300)
paint.fill(False)

paint.fill(True)
for x in range(4):
  paint.right(90)
  paint.forward(100)
paint.fill(False)

paint.fill(True)
for x in range(4):
  paint.right(90)
  paint.forward(100)
paint.fill(False)

paint.fill(True)
paint.left(90)
for x in range(4):
  paint.forward(100)
  paint.left(90)
paint.fill(False)

paint.fill(True)
paint.forward(100)
for x in range(4):
  paint.forward(100)
  paint.left(90)
paint.fill(False)

paint.forward(100)
paint.fill(True)
for x in range(4):
  paint.forward(100)
  paint.left(90)
paint.fill(False)

paint.fill(True)
paint.forward(140)
paint.left(90)
paint.forward(1)
paint.left(90)
paint.forward(3)
paint.right(36)
paint.forward(10)
paint.left(5)
paint.forward(10)
paint.right(20)
paint.forward(30)
paint.left(70)
paint.forward(115)
paint.fill(False)

paint.penup()
paint.home()
paint.left(180)
paint.pendown()
paint.fill(True)
paint.forward(200)
paint.right(90)
paint.forward(600)
paint.right(90)
paint.forward(200)
paint.fill(False)
paint.pencolor("#440024")
paint.backward(300)
paint.forward(1100)
paint.left(110)
paint.forward(150)
paint.left(70)
paint.forward(1000)
paint.left(110)
paint.forward(150)
