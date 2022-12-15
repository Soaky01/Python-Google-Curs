from tkinter import *

root = Tk()

# Create a label to display the result
result_label = Label(root, text="0", font=("Helvetica", 20))
result_label.grid(row=0, column=0, columnspan=4)

# Create buttons for the numbers
number_buttons = []
for i in range(3):
    number_buttons.append([])
    for j in range(3):
        number_buttons[i].append(Button(root, text=str(i*3+j+1), font=("Helvetica", 20)))
        number_buttons[i][j].grid(row=i+1, column=j)

# Create the "0" button
zero_button = Button(root, text="0", font=("Helvetica", 20))
zero_button.grid(row=4, column=0)

# Create the "." button
dot_button = Button(root, text=".", font=("Helvetica", 20))
dot_button.grid(row=4, column=1)

# Create the "=" button
equal_button = Button(root, text="=", font=("Helvetica", 20))
equal_button.grid(row=4, column=2)

# Create the "+" button
plus_button = Button(root, text="+", font=("Helvetica", 20))
plus_button.grid(row=1, column=3)

# Create the "-" button
minus_button = Button(root, text="-", font=("Helvetica", 20))
minus_button.grid(row=2, column=3)

# Create the "*" button
multiply_button = Button(root, text="*", font=("Helvetica", 20))
multiply_button.grid(row=3, column=3)

# Create the "/" button
divide_button = Button(root, text="/", font=("Helvetica", 20))
divide_button.grid(row=4, column=3)

# Create the "C" button
clear_button = Button(root, text="C", font=("Helvetica", 20))
clear_button.grid(row=1, column=4)

root.mainloop()
