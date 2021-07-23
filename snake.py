import os
import turtle
import time
import random

#variables
score = 0
highest_score = 0
delay = 0.1

#set up the screen window
window =turtle.Screen()
window.title("Snake Game 🐍")
window.setup(width=600, height=600)
window.bgcolor("black")
window.tracer(0) # setup delay



#set up Snack
snack = turtle.Turtle()
snack.speed(0)
snack.shape("square")
snack.color("green")
snack.penup()
snack.goto(0,0)
snack.direction ="stop" #not going any direction


#snack food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)


#ScreenBoard

scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.shape("square")
scoreboard.color("yellow")
scoreboard.penup()
scoreboard.hideturtle() #no arch in the screen

scoreboard.goto(0,260)
scoreboard.write("SCORE: {}   HIGHEST SCORE:   {}".format(score, highest_score), align="center",
                             font=("ds-digital", 24, "normal"))

#Funtions

def go_up():

        snack.direction ="up"
def go_down():

        snack.direction="down"
def go_left():

        snack.direction="left"

def go_right():

        snack.direction="right"

def move():
    if snack.direction =="up":
        y = snack.ycor()
        snack.sety(y+20)
    if snack.direction =="down":
        y = snack.ycor()
        snack.sety(y-20)
    if snack.direction == "left":
        x = snack.xcor()
        snack.setx(x-20)
    if snack.direction == "right":
        x = snack.xcor()
        snack.setx(x+20)

#Keyboard control

window.listen()
window.onkeypress(go_up,"w")
window.onkeypress(go_down,"s")
window.onkeypress(go_left,"a")
window.onkeypress(go_right,"d")

segments =[]

while True:
    window.update()

    if snack.xcor() > 290 or snack.xcor() <-290 or snack.ycor() >290 or snack.ycor() <-290:
        time.sleep(1)
        snack.goto(0,0)
        snack.direction ="stop"

        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score = 0
        delay = 0.1

        scoreboard.clear()
        scoreboard.write("SCORE: {} HIGHEST SCORE:  {}".format(score,highest_score),align="center",font = ("ds-digital",24,"normal"))

    if snack.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)


        delay -=0.001
        score +=10

        if(score > highest_score):
            highest_score = score
        scoreboard.clear()

        scoreboard.write("Score: {}   High Score:   {}".format(score,highest_score),align="center",font=("ds-digital",24,"normal"))


    for i in range(len(segments)-1,0,-1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)

    if len(segments) > 0:
        x = snack.xcor()
        y = snack.ycor()
        segments[0].goto(x,y)
    move()

    for segment in segments:
        if segment.distance(snack) <20:
            time.sleep(1)
            snack.goto(0,0)
            snack.direction="stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            scoreboard.clear()
            scoreboard.write("Score: {}   High Score:   {}".format(score, highest_score), align="center",
                             font=("ds-digital", 24, "normal"))
    time.sleep(delay)

window1.mainloop()