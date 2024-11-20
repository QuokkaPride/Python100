from tkinter import *
import tkinter.font as tkFont  # Import the font module

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

my_label = Label(text="Miles to Km Converter\nfor Conservatives", font=("Arial", 20, "bold"))
my_label.grid(row=1, column=2)

# Define a font for the Entry widget
entry_font = tkFont.Font(family="Arial", size=20)

# Miles Entry
input = Entry(width=10, font=entry_font)  # Apply the font to the Entry widget
input.grid(row=2, column=2)

# Miles Label
miles_label = Label(text="Miles", font=("Arial", 20, "normal"))
miles_label.grid(row=2, column=3)

# is equal Label
equal_label = Label(text="is equal to", font=("Arial", 20, "normal"))
equal_label.grid(row=3, column=1)

# km output label
km_output_label = Label(text="0", font=("Arial", 20, "normal"))
km_output_label.grid(row=3, column=2)

# km label
km_label = Label(text="Km", font=("Arial", 20, "normal"))
km_label.grid(row=3, column=3)

# Define the function before calling it
def button_clicked():
    mk_output = round(float(input.get()) * 1.60934, 1)
    km_output_label.config(text=mk_output)

# button
button = Button(text="Calculate", command=button_clicked)
button.grid(row=4, column=2)

window.mainloop()
