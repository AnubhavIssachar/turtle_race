from turtle import Turtle, Screen
import random

screen = Screen()
user_bet = screen.textinput(title="Make a bet", prompt="Guess which turtle will win the race (VIBGYOR)")
screen.setup(width=500, height=350)
speeds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Adjusted speeds, starting from 1
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
positions = [-100, -75, -50, -25, 0, 25, 50]
all_turtles = []

# Create turtles and position them
for i in range(len(colors)):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(-230, positions[i])
    all_turtles.append(tim)

if user_bet:
    while True:
        for t in all_turtles:
            t.forward(random.choice(speeds))  # Randomly choose speed from speeds list
            if t.xcor() > 230:
                winning_color = t.fillcolor()
                if winning_color == user_bet:
                    print(f"You have won!!!! {winning_color} turtle won the race!!!")
                else:
                    print(f"You have lost!!!! {winning_color} turtle won the race!!!")
                screen.bye()  # Close the turtle graphics window after displaying result
                break  # Exit the inner loop once a turtle crosses the finish line
        if any(t.xcor() > 230 for t in all_turtles):
            break  # Exit the outer loop after determining the race outcome

