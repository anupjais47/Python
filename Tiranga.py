import turtle
colors =['red','white','green','orange','yellow']
# colors =['saffron','white','green']
t=turtle.Pen()
# turtle.bgcolor('black')
turtle.bgcolor('blue')
for x in range(360):
    t.pencolor(colors[x%6])
    # t.pencolor(colors[x%3])
    t.width(x//100+1)
    t.forward(x)
    t.left(59)