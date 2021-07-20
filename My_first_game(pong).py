#Pong
import turtle
import winsound
win=turtle.Screen()
win.title("Pong(First Game)")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)


#Score
score_a=0
score_b=0

#paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("cyan")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("cyan")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


#paddle c
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx=0.25
ball.dy=-0.25

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("orange")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 PlayerB: 0",align="center",font=("Courier",16,"normal"))

#Function
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)


def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)


def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)



#Keyboard binding
win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")


#Main game loop
while True:
    win.update()


    #Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border Checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {} PlayerB: {}".format(score_a,score_b),align="center",font=("Courier",16,"normal"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {} PlayerB: {}".format(score_a,score_b),align="center",font=("Courier",16,"normal"))
    

    #Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor()>paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    if (ball.xcor() < -340 and ball.xcor() >-350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor()>paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
