from turtle import Turtle, Screen
import random

screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? enter color: ")
while user_bet not in colors:
    user_bet = screen.textinput(title="Make your bet", prompt="Error, pick a color from the rainbow:  ")

all_turtles = []
y_coordinate = -70
for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinate + 20)
    y_coordinate = new_turtle.ycor()
    new_turtle.speed('fastest')
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


def run_program(race_on):
    while race_on:
        for turtle in all_turtles:
            if turtle.xcor() >= 230:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You have won, the {winning_color} turtle has won!")
                else:
                    print(f"You have lost, the {winning_color} turtle has won")
                return
            else:
                random_distance = random.randint(0, 10)
                turtle.forward(random_distance)


run_program(is_race_on)

screen.exitonclick()
