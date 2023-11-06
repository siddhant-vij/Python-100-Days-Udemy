import tkinter as tk


window = tk.Tk()
window.title("GUI Calculators")
window.minsize(width=200, height=100)


def menuBarDisplay():
    menuBar = tk.Menu(window)
    window.config(menu=menuBar)
    calcMenu = tk.Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Convert", menu=calcMenu)
    calcMenu.add_command(label="Miles to Km", command=milesToKmDisplay)
    calcMenu.add_command(label="Km to Miles", command=kmToMilesDisplay)
    calcMenu.add_command(label="°F to °C", command=fToCDisplay)
    calcMenu.add_command(label="°C to °F", command=cToFDisplay)
    calcMenu.add_separator()
    calcMenu.add_command(label="Exit", command=window.quit)


def clearWindowAndDisplayMenu():
    for widget in window.winfo_children():
        widget.destroy()
    menuBarDisplay()


def milesToKm(milesInput, kmResultLabel):
    miles = float(milesInput.get())
    km = miles * 1.60934
    kmResultLabel.config(text=f"{km:.2f}")


def milesToKmDisplay():
    clearWindowAndDisplayMenu()

    milesInput = tk.Entry()
    milesInput.grid(column=1, row=0)

    milesLabel = tk.Label(text="Miles")
    milesLabel.grid(column=2, row=0)

    isEqualLabel = tk.Label(text="is equal to")
    isEqualLabel.grid(column=0, row=1)

    kmResultLabel = tk.Label(text="0")
    kmResultLabel.grid(column=1, row=1)

    kmLabel = tk.Label(text="Km")
    kmLabel.grid(column=2, row=1)

    calculateButton = tk.Button(
        text="Calculate", command=lambda: milesToKm(milesInput, kmResultLabel))
    calculateButton.grid(column=1, row=2)


def kmToMiles(kmInput, milesResultLabel):
    km = float(kmInput.get())
    miles = km / 1.60934
    milesResultLabel.config(text=f"{miles:.2f}")


def kmToMilesDisplay():
    clearWindowAndDisplayMenu()

    kmInput = tk.Entry()
    kmInput.grid(column=1, row=0)

    kmLabel = tk.Label(text="Km")
    kmLabel.grid(column=2, row=0)

    isEqualLabel = tk.Label(text="is equal to")
    isEqualLabel.grid(column=0, row=1)

    milesResultLabel = tk.Label(text="0")
    milesResultLabel.grid(column=1, row=1)

    milesLabel = tk.Label(text="Miles")
    milesLabel.grid(column=2, row=1)

    calculateButton = tk.Button(
        text="Calculate", command=lambda: kmToMiles(kmInput, milesResultLabel))
    calculateButton.grid(column=1, row=2)


def fToCCalc(fInput, cResultLabel):
    f = float(fInput.get())
    c = (f - 32) * 5 / 9
    cResultLabel.config(text=f"{c:.2f}")


def fToCDisplay():
    clearWindowAndDisplayMenu()

    fInput = tk.Entry()
    fInput.grid(column=1, row=0)

    fLabel = tk.Label(text="°F")
    fLabel.grid(column=2, row=0)

    isEqualLabel = tk.Label(text="is equal to")
    isEqualLabel.grid(column=0, row=1)

    cResultLabel = tk.Label(text="0")
    cResultLabel.grid(column=1, row=1)

    cLabel = tk.Label(text="°C")
    cLabel.grid(column=2, row=1)

    calculateButton = tk.Button(
        text="Calculate", command=lambda: fToCCalc(fInput, cResultLabel))
    calculateButton.grid(column=1, row=2)


def cToFCalc(cInput, fResultLabel):
    c = float(cInput.get())
    f = c * 9 / 5 + 32
    fResultLabel.config(text=f"{f:.2f}")


def cToFDisplay():
    clearWindowAndDisplayMenu()

    cInput = tk.Entry()
    cInput.grid(column=1, row=0)

    cLabel = tk.Label(text="°C")
    cLabel.grid(column=2, row=0)

    isEqualLabel = tk.Label(text="is equal to")
    isEqualLabel.grid(column=0, row=1)

    fResultLabel = tk.Label(text="0")
    fResultLabel.grid(column=1, row=1)

    fLabel = tk.Label(text="°F")
    fLabel.grid(column=2, row=1)

    calculateButton = tk.Button(
        text="Calculate", command=lambda: cToFCalc(cInput, fResultLabel))
    calculateButton.grid(column=1, row=2)



menuBarDisplay()
window.mainloop()
