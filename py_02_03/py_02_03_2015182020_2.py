import turtle as t

x = -300
size = 0
size1 = 100
size2 = 500
count = 0
while(count <= 5):
    t.penup()
    t.goto(count * size1 + x, size2 + x)
    t.pendown()
    t.goto(count * size1 + x, size + x)
    count = count + 1


count = 0
while(count <= 5):
    t.penup()
    t.goto(size + x, count * size1 + x)
    t.pendown()
    t.goto(size2 + x, count * size1 + x)
    count = count + 1

t.exitonclick()
