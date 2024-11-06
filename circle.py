import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")

t.speed(0) 
t.width(2) 
n=40 
h=0    

for i in range(n * 2):
    c=colorsys.hsv_to_rgb(h, 1, 0.9)  
    h+=1/n                          
    t.color(c)                         
    t.forward(i * 2)                   
    t.right(89)
    for j in range(6):                 
        t.forward(100)
        t.right(60)
t.hideturtle()
turtle.done()
