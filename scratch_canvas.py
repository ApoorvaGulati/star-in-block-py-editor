import turtle

turtle.color('gold', 'gold')

turtle.begin_fill()
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
points = 0
while points < 5:
      turtle.forward(250)
      turtle.left(144)
      points=points + 1
turtle.end_fill()