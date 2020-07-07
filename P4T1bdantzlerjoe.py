# Initials
# 7/5/2020
# CTI-110 P4T2 - Initials
# Joe Dantzler

import turtle
turtle.setup(900,400)#make the window 900 400
wn = turtle.Screen()
wn.title("Turtle writing Initials")#title of the window
wn.bgcolor("lightgreen")#change the backward color to lightgreen

turtle.width(100)
# turtle.penize(30)

t = turtle.Turtle()
t.pensize(10)#setting the pen size to 10
t.color("purple")#setting the turtle color to purple
t.up()#pen up
#this will move the turtle to left upeer corner
t.backward(360)
t.left(90)
t.forward(80)
t.right(90)
#now down the turtle to draw
t.down()
#drawing the Z
t.forward(180)#now forward to the 180
t.right(135)#make the right turn with 135 angle
t.forward(250)#now forward upto 250
t.left(135)#take the turn to left 135 angle
t.forward(180)#and forward to 180

t.up()#up the turtle
t.color("blue")#set the color blue
t.forward(20)#go forward to 20
t.left(90)#and take 90 to left
t.down()# down the pen
#this will draw the F
t.forward(180)#go forward to 180
t.right(90)#then take 90 turn to the right
t.forward(150)#then go forward 150
t.backward(150)#now come backward to 150
t.right(90)#make the right turn to 90
t.forward(90)#go forward to 90
t.left(90)#take 90 angle to left and
t.forward(150)#go forward to 150
