import turtle
tao = turtle.Pen
tao = turtle.Pen()
tao.shape("turtle")

def Octagon():
    for i in range(8):
        tao.fd(20)
        tao.left(45)

def Triangle():
    tao.fd(100)
    tao.rt(115)
    tao.fd(100)
    tao.rt(122)
    tao.fd(108)
    tao.rt(33)

def Circle():
    for i in range(8):
        tao.circle(8)
        tao.rt(45)
    

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()


Go(50,50)
Octagon()
Go(-50,-50)
Triangle()
Go(-50,50)
Octagon()
Go(15,15)
Circle()
Go(100,50)
