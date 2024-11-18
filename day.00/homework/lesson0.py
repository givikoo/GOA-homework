from turtle import *





width(7)
 
color("purple")

#we want to paint a house

#step 1 : draw a square
speed(30)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("yellow")
color("yellow")
begin_fill()
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200) 
pendown()
 
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a aquare

#drawimg windows

right(0)
forward(5)
color("brown")
begin_fill()

penup()
goto(20, 200)
pendown()
right(330)
forward(10)
right(0)
forward(100)
right(270)
forward(35)
right(270)
forward(110)
right(270)
forward(30)
penup()
goto(180, 200)
pendown()
right(270)
forward(110)
right(90)
forward(20)
forward(0)
forward(10)
right(90)
forward(110)
right(90)
forward(30)


exitonclick()