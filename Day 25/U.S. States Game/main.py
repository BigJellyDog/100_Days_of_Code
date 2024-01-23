from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.setup(725, 491)
screen.screensize(725, 491)
screen.bgpic("blank_states_img.gif")
data = pandas.read_csv("50_states.csv")
tim = Turtle()
tim.penup()
tim.hideturtle()

states = data.state.to_list()
x = data.x.to_list()
y = data.y.to_list()


data_dir = {
    "states": states,
    "x": x,
    "y": y,
}


"""Game logic"""
game = True
correct = 0
correct_list = []
while game:
    if correct == 50:
        screen.clear()
        tim.pencolor("white")
        tim.goto(0, 0)
        screen.bgcolor("black")
        tim.pendown()
        tim.write("YOU WIN! CONGRATULATIONS!!!", align="center", font=('Courier', 25, 'normal'))
        break
    answer_state = screen.textinput(f"{correct}/50 States Correct", "Enter state name: ").title()
    if answer_state in data_dir["states"]:
        position = data_dir["states"].index(answer_state)
        print(len(data_dir["states"]))
        position_x = data_dir["x"][position]
        position_y = data_dir["y"][position]
        tim.goto(position_x, position_y)
        tim.pendown()
        tim.write(f"{answer_state}")
        tim.penup()
        if answer_state not in correct_list:
            correct_list.append(answer_state)
            correct += 1


screen.mainloop()
