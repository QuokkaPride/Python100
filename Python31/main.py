from tkinter import *
import pandas as pd
import random

known_words = []
trouble_words = []
# Create the main window first
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Load images first - move these up before they're used
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# Create UI
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)
canvas.bind("<Button-1>", lambda event: flip_card())

# Add this line before the functions
flip_timer = None  # Initialize the timer variable

# functions
def get_random_word():
    global random_word, flip_timer
    if flip_timer:  # Only try to cancel if there is an existing timer
        window.after_cancel(flip_timer)
    canvas.delete("all")
    
    # Show the front of the card
    canvas.create_image(400, 263, image=front_image)
    random_word = random.choice(data_dict)
    canvas.create_text(400, 130, text="French", font=("Arial", 40, "italic"))
    canvas.create_text(400, 263, text=random_word["French"], font=("Arial", 60, "bold"))
    
    # Schedule the card flip after 3 seconds
    flip_timer = window.after(3000, flip_card)

def flip_card():
    # Show the back of the card
    canvas.delete("all")
    canvas.create_image(400, 263, image=back_image)
    canvas.create_text(400, 130, text="English", font=("Arial", 40, "italic"))
    canvas.create_text(400, 263, text=random_word["English"], font=("Arial", 60, "bold"))

def next_card():
    trouble_words.append(random_word)
    csv_data = pd.DataFrame(trouble_words)
    csv_data.to_csv("data/trouble_words.csv", index=False)
    get_random_word()

def is_known():
    known_words.append(random_word)
    csv_data = pd.DataFrame(known_words)
    csv_data.to_csv("data/known_words.csv", index=False)
    data_dict.remove(random_word)
    next_card()

# read the csv file and create dictionary
data = pd.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")

# Now we can safely call get_random_word() since front_image is defined
get_random_word()

# Create buttons
button_wrong = Button(image=wrong_image, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=0)

button_right = Button(image=right_image, highlightthickness=0, command=is_known)
button_right.grid(row=1, column=1)

# Add this at the end to run the application
window.mainloop()