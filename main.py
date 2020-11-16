import turtle
# from csv_model import CsvModel
import pandas as pd

# models = {}
screen = turtle.Screen()
screen.title("US States")
img_loc = "blank_states_img.gif"
screen.addshape(img_loc)
turtle.shape(img_loc)
# turt = {"key": turtle.Turtle()}


c = 0


def Game():
    global c
    answer = screen.textinput(f"Name The state Of USA ({c}/50) ", "Enter the states of USA one by one")
    name_of_states = pd.read_csv("./50_states.csv")
    states = name_of_states["state"].tolist()
    if answer in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_ans = name_of_states[name_of_states.state == answer]
        t.goto(int(state_ans.x), int(state_ans.y))

        c = c + 1
        t.write(answer)


while c != 50:
    Game()

turtle.mainloop()

# turtle.onscreenclick(get_mouse_click)


# screen.exitonclick()


# for get coordinates
# def get_mouse_click(x,y):
#     print(x,y)
