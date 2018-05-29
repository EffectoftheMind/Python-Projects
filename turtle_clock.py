import turtle
import time
import replit


paint = turtle.Turtle()
paint.shape("turtle")
paint.color("purple")
paint.speed("fastest")

wn = turtle.Screen()
wn.bgcolor("#A0F1D8")

for tick in range(12):
  paint.up()
  paint.forward(80)
  paint.down()
  paint.forward(10)
  paint.up()
  paint.forward(30)
  paint.stamp()
  paint.backward(120)
  paint.left(30)
  
paint.ht()

second = turtle.Turtle()
second.speed("instant")
second.color("red")

minute = turtle.Turtle()
minute.speed("instant")

hour = turtle.Turtle()
hour.speed("instant")
hour.pensize(10)

update = True
updatemin = True
updatehour = True

while True:
  b = time.gmtime(time.time())
  b = time.localtime()
  min = b.tm_min
  sec = b.tm_sec
  if update:
    #second hand
    second.left(90)
    second.pensize(3)
    second.right((min)*6)
    second.forward(120)
    update = False
  if updatemin:
    #minute hand
    minute.left(90)
    minute.pensize(3)
    minute.right((sec)*6)
    minute.forward(120)
    updatemin = False
  if updatehour:
    #hour hand
    hour.left(90)
    hour.pensize(10)
    hour.right(((b.tm_hour)%12)*30+min*0.5)
    hour.forward(120)
    updatehour = False
  time.sleep(0.1)
  replit.clear()
  b = time.gmtime(time.time())
  b = time.localtime()

  new_min = b.tm_min
  new_sec = b.tm_sec
  
  if new_min != min:
    updatemin = True
    minute.home()
    minute.clear()
  
  if new_sec != sec:
    update = True
    second.home()
    second.clear()
