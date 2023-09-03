import turtle
import random

screen = turtle.Screen()
screen.title("Catch The Turtle")
screen.bgcolor("#99FFFF")
screen.setup(width=600, height=400)

player = turtle.Turtle()
player.shape("turtle")
player.color("#330019")
player.penup()
player.speed(0)

turtles = []

score = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 170)
score_display.write("Puan : {}".format(score), align="center", font=("Arial", 20, "normal"))


def create_turtle():
    new_turtle = turtle.Turtle()
    new_turtle.shape("turtle")
    new_turtle.color("red")
    new_turtle.penup()
    new_turtle.speed(1)
    x = random.randint(-280, 280)
    y = random.randint(-180, 180)
    new_turtle.goto(x, y)
    turtles.append(new_turtle)

for _ in range(5):
    create_turtle()

def move_player(x, y):
    player.goto(x, y)

def check_collisions():
    global score
    for turtle in turtles:
        if player.distance(turtle) < 20:
            turtles.remove(turtle)
            turtle.hideturtle()
            create_turtle()
            score += 1
            score_display.clear()
            score_display.write("Puan : {}".format(score), align="center", font=("Arial", 20, "normal"))

screen.listen()
screen.onkeypress(screen.bye, "q")
screen.onscreenclick(move_player)

while True:
    check_collisions()
    screen.update()
