#Repeating Squares
#7/4/2020
#CTI-110 P4T1a-Repeating Squares
#Joe Dantzler
# Draw a loop that draws a square
#Write a program that uses nested loops to draw 100 squares


import turtle

turtle.right(180)

turtle.speed(0)

length = 505

for times in range (100):
  for endtimes in range (4):
    turtle.forward(length)
    turtle.right(90)
  length -= 5
