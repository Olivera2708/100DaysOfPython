import turtle
import pandas
from pandas.core.dtypes import missing

screen = turtle.Screen()
screen.title("State Game")
screen.setup(725, 491)
image = "C:/Users/Olivera/Documents/Python learning/Day25-USAStatesGame/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

result = 0
guessed_states = []
missing_states = []

data = pandas.read_csv("C:/Users/Olivera/Documents/Python learning/Day25-USAStatesGame/50_states.csv")
states = data["state"].to_list()
x_cor = data["x"].to_list()
y_cor = data["y"].to_list()

while result != 50:
    answer_state = screen.textinput(f"{result}/50 States correct", "What's another state's name?")
    if answer_state == "exit":
        # for state in states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("C:/Users/Olivera/Documents/Python learning/Day25-USAStatesGame/states_to_learn.csv")
        screen.bye()
        break
    for number in range(len(states)):
        if states[number].lower() == answer_state.lower():
            guessed_states.append(states[number])
            result += 1
            point = turtle.Turtle()
            point.hideturtle()
            point.penup()
            point.goto(x_cor[number], y_cor[number])
            point.write(f"{states[number]}", align="center", font=("Courier", 10, "bold"))
            
screen.exitonclick()