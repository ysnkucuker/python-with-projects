from tkinter import *

window = Tk()
window.title("BMI Index")
window.minsize(width=400, height=300)
window.config(padx=20, pady=20)

weight_label = Label(text="Enter your weight")
weight_label.config(font=("Verdana", 12))
weight_label.config(padx=20, pady=20)
weight_label.pack()

weight_entry = Entry(width=20)
weight_entry.pack()

height_label = Label(text="Enter your height")
height_label.config(font=("Verdana", 12))
height_label.config(padx=20, pady=20)
height_label.pack()

height_entry = Entry(width=20)
height_entry.pack()

warning_label = Label(text="")
warning_label.config(font=("Verdana", 12))
warning_label.config(padx=20, pady=20)

def resultbmi(bmi):
    result_string = f"Your bmi is : {round(bmi,2)}. You are "
    if bmi <= 16:
        result_string += "severaly thin!"
    elif bmi > 16 and bmi <= 17:
        result_string += "modaretly thin!"
    elif bmi > 17 and bmi <= 18.5:
        result_string += "mild thin!"
    elif bmi > 18.5 and bmi <= 25:
        result_string += "normal!"
    elif bmi > 25 and bmi <= 30:
        result_string += "overweight!"
    elif bmi > 30 and bmi <= 35:
        result_string += "obese class 1!"
    elif bmi > 35 and bmi <= 40:
        result_string += "obese class 2!"
    return result_string

def button_clicked():
    try:
        warning_label.config(text="")
        weight = int(weight_entry.get())
        height = int(height_entry.get())
        if (weight == " "):
            warning_label.config(text="Enter your weight")
            warning_label.pack()
        if (height == " "):
            warning_label.config(text="Enter your height")
            warning_label.pack()
    except ValueError:
        warning_label.config(text="Please enter a number")
        warning_label.pack()
    bmi = float(weight) / (float(height)/100) ** 2
    warning_label.config(text=resultbmi(bmi))
    warning_label.pack()


button = Button(text="Calculate", command=button_clicked)
button.config(padx=5, pady=5)
button.pack()

window.mainloop()