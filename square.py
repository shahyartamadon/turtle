import turtle
t=turtle
t.Screen().bgcolor(0,0.3,0.5)
for x in range(0,18):
    t.color(1,1,0)
    t.begin_fill()
    for y in range(0,4):
        t.fd(100)
        t.lt(90)
    t.end_fill()
    t.lt(20)
    
