import turtle
import time
class FPS:
    def __init__(self) :

        self._tick2_frame=0
        self._tick2_fps=20000000 # real raw FPS
        self._tick2_t0=time.time()

    def fpsLimit(self,fps=60):
        global _tick2_frame,_tick2_fps,_tick2_t0
        n=self._tick2_fps/fps
        self._tick2_frame+=n
        while n>0: n-=1
        if time.time()-self._tick2_t0>1:
            _tick2_t0=time.time()
            _tick2_fps=self._tick2_frame
            _tick2_frame=0


win=turtle.Screen()
win.title('PingPong')
win.bgcolor('black')
#win.bgpic('Gamegif.gif')
win.setup(width=1100, height=1000)
win.tracer(0)

#Border
up_border=turtle.Turtle()
up_border.speed(0)
up_border.shape('square')
up_border.color('green')
up_border.shapesize(stretch_wid=1,stretch_len=50)
up_border.penup()
up_border.goto(0,420)


low_border=turtle.Turtle()
low_border.speed(0)
low_border.shape('square')
low_border.color('green')
low_border.shapesize(stretch_wid=1,stretch_len=50)
low_border.penup()
low_border.goto(0,-420)

right_border=turtle.Turtle()
right_border.speed(0)
right_border.shape('square')
right_border.color('green')
right_border.shapesize(stretch_wid=43,stretch_len=1)
right_border.penup()
right_border.goto(490,0)


left_border=turtle.Turtle()
left_border.speed(0)
left_border.shape('square')
left_border.color('green')
left_border.shapesize(stretch_wid=43,stretch_len=1)
left_border.penup()
left_border.goto(-490,0)



#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color('red')
pen.penup()
pen.hideturtle()
pen.goto(0,450)
pen.write('Level: 0', align='center',font=('Courier',24,'normal'))

#Score
score=0

#pad a
pad_a=turtle.Turtle()
pad_a.speed(0)
pad_a.shape('square')
pad_a.color('white')
pad_a.shapesize(stretch_wid=0.5,stretch_len=5)
pad_a.penup()
pad_a.goto(-420,-400)
pad_a.dx=1

#pad b
pad_b=turtle.Turtle()
pad_b.speed(0)
pad_b.shape('square')
pad_b.color('white')
pad_b.shapesize(stretch_wid=0.5,stretch_len=5)
pad_b.penup()
pad_b.goto(420,-300)
pad_b.dx=1

#pad c
pad_c=turtle.Turtle()
pad_c.speed(0)
pad_c.shape('square')
pad_c.color('white')
pad_c.shapesize(stretch_wid=0.5,stretch_len=5)
pad_c.penup()
pad_c.goto(-300,-200)
pad_c.dx=1

#pad d
pad_d=turtle.Turtle()
pad_d.speed(0)
pad_d.shape('square')
pad_d.color('white')
pad_d.shapesize(stretch_wid=0.5,stretch_len=5)
pad_d.penup()
pad_d.goto(250,-100)
pad_d.dx=1

#pad e
pad_e=turtle.Turtle()
pad_e.speed(0)
pad_e.shape('square')
pad_e.color('white')
pad_e.shapesize(stretch_wid=0.5,stretch_len=5)
pad_e.penup()
pad_e.goto(-200,0)
pad_e.dx=1

#pad f
pad_f=turtle.Turtle()
pad_f.speed(0)
pad_f.shape('square')
pad_f.color('white')
pad_f.shapesize(stretch_wid=0.5,stretch_len=5)
pad_f.penup()
pad_f.goto(100,100)
pad_f.dx=1

#pad G
pad_g=turtle.Turtle()
pad_g.speed(0)
pad_g.shape('square')
pad_g.color('white')
pad_g.shapesize(stretch_wid=0.5,stretch_len=5)
pad_g.penup()
pad_g.goto(270,200)
pad_g.dx=1

#pad h
pad_h=turtle.Turtle()
pad_h.speed(0)
pad_h.shape('square')
pad_h.color('white')
pad_h.shapesize(stretch_wid=0.5,stretch_len=5)
pad_h.penup()
pad_h.goto(-300,300)
pad_h.dx=1

l=[pad_a,pad_b,pad_c,pad_d,pad_e,pad_f,pad_g,pad_h]


#Ball
b=turtle.Turtle()
b.speed(0)
b.shape('circle')
b.color('blue')

b.penup()
b.goto(pad_a.xcor(),pad_a.ycor()+20)
b.dx=0
b.dy=-1


def ballMove():
    b.sety(b.ycor()+110)



#Keyboard Binding
win.listen()
win.onkeypress(ballMove,'space')


s=0

fps=FPS()
while True:
    fps.fpsLimit(300)
    win.update()

    if b.ycor() < 420 and b.ycor()>-420:
        colPad=None
        col=False


        # Gravity of ball


        for pad in l:

            if (b.xcor() <= pad.xcor() + 50 and b.xcor() >= pad.xcor() - 50) and b.ycor()<pad.ycor()+17 and b.ycor()>pad.ycor()+15:
                colPad=pad
                col=True
                break

        if col:

            b.setx(b.xcor()+colPad.dx)
        else:

            b.sety(b.ycor()+b.dy)


        for pad in l:
            pad.setx(pad.xcor() + pad.dx)

            if pad.xcor() > 420 or pad.xcor() < -420:
                pad.dx *= -1




        if colPad==pad_h:
            for pad in l:
                if pad.dx< 0:
                    pad.dx-=0.35
                else:
                    pad.dx+=0.35
            score+=1
            pen.clear()
            pen.write('Level: '+str(score),align='center',font=('Courier',24,'normal'))

            b.goto(pad_a.xcor(),pad_a.ycor()+20)
    else:

        pen.clear()
        pen.goto(0,0)
        pen.write('Your score is:' + str(score), align='center', font=('Courier', 50, 'normal'))

