import turtle
col=('red','yellow','green','cyan','blue','white')
t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
t.speed(300)
for i in range(500):
    t.color(col[i%6])
    t.forward(i*4)
    t.left(150)
    t.width(5)
