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
game_over = False

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 170)
score_display.write("Puan : {}".format(score), align="center", font=("Arial", 20, "normal"))

count_down_turtle = turtle.Turtle()
count_down_turtle.speed(0)
count_down_turtle.color("black")
count_down_turtle.penup()
count_down_turtle.hideturtle()
count_down_turtle.goto(0, 140)
count_down_turtle.write("Süre : {}".format(score), align="center", font=("Arial", 20, "normal"))


def countdown(time):
    global game_over
    count_down_turtle.hideturtle()
    count_down_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    count_down_turtle.setposition(0,y)
    count_down_turtle.clear()

    if time > 0:
       count_down_turtle.clear()
       screen.ontimer(lambda : countdown(time - 1),1000)
       count_down_turtle.goto(0, 120)
       count_down_turtle.write("Süre : {}".format(time), align="center", font=("Arial", 20, "normal"))
    else:
        game_over = True
        count_down_turtle.clear()
        count_down_turtle.goto(0, 90)
        count_down_turtle.write("Oyun Bitti!!!", align="center", font=("Arial", 20, "normal"))

countdown(10)

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
    if not game_over:
        pass
    else:
        player.clear()
        score_display.clear()
        turtles.clear()
        turtle.hideturtle()
