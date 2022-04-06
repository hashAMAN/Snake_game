import turtle
import time
import random
delay=0.1
score=0
high_score=0
wn=turtle.screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)
head=turtle.Turtle()