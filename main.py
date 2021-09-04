import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgcolor("black")
screen.addshape(image)

turtle.shape(image)
tim = Turtle()
tim.hideturtle()

tim.shape("turtle")
tim.penup()
tim.speed("fastest")
tim.goto(900, 900)
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)




data = pandas.read_csv("50_states.csv")
allStates = data.state.to_list()
guessStates = []
statesAnswered=0
while len(guessStates) < 50:

    answerState = screen.textinput(title=f"{statesAnswered}/50 left", prompt="What's another state's name?").title()
    if answerState=="Exit":
        missingStates=[states for states in allStates if states not in guessStates ]
    #     for state in allStates:
    #         if state not in guessStates:
    #             missingStates.append(state)
        newData=pandas.DataFrame(missingStates)
        newData.to_csv("states to remember")
        break
    if answerState in allStates :
        stateData = data[data.state == answerState]
        tim.goto(int(stateData.x), int(stateData.y))
        tim.write(answerState)
        guessStates.append(answerState)
        statesAnswered+=1
    else:
        print("Incorrect name")



















#     answer = data[data.state == answerState"]
#     print(answer.x[1])
#     xCor=answer.x
#     yCor=answer.y
#     print("ewqr")
#
#     tim.goto(int(xCor),int(yCor))
#     tim.write(f"{answerState}")
#
#
# else:
#     print("klsd;ajas;f")


# if answerState in allStates:
#     stateData=data[data.state==answerState]
#     tim.goto(int(stateData.x),int(stateData.y))
#     tim.write(answerState)



