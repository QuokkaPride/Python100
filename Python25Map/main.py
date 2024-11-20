import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

# Set up the screen size and position
screen.setup(width=800, height=600, startx=100, starty=100)

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")

tim = turtle.Turtle()
tim.hideturtle()
tim.penup()

# Initialize correct_guesses as an empty list
correct_guesses = []

number_of_correct_guesses = len(correct_guesses)
message = f"Name a state:"

# Extract all state names from the data
all_states = data.state.to_list()

#get state
while number_of_correct_guesses < 50:
    state_guess = screen.textinput(f"{number_of_correct_guesses}/50 States Correct", message).title()
    if state_guess == "Exit":
        break
    row = data[data.state == state_guess]
    if not row.empty:
        correct_guesses.append(state_guess)
        number_of_correct_guesses = len(correct_guesses)  # Update the count
        x_cor = int(row.x)
        y_cor = int(row.y)

        #write state name on map
        tim.goto(x_cor, y_cor)
        tim.write(state_guess)
        message = f"You're right! Name another state:"
    else:
        message = f"Get it together Samantha, try again:"
    
    # Calculate and print the list of states not yet guessed
    states_not_guessed = [state for state in all_states if state not in correct_guesses]
    print("States not guessed yet:", states_not_guessed)
    
    print(number_of_correct_guesses)
    print(correct_guesses)

if number_of_correct_guesses == 50:
    message = "You've guessed all the states! You win!"

df = pd.DataFrame(states_not_guessed)
df.to_csv("states_to_learn.csv")


turtle.mainloop()
screen.exitonclick()