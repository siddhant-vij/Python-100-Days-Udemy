import tkinter as tk

window = tk.Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)


def click():
    label.config(text=input.get())


label = tk.Label(text="I am a label")
label.grid(column=0, row=0)
label.config(padx=50, pady=50)

button = tk.Button(text="Click Me", command=click)
button.grid(column=1, row=1)

newButton = tk.Button(text="New Button", command=click)
newButton.grid(column=2, row=0)

input = tk.Entry()
input.grid(column=3, row=2)


window.mainloop()
