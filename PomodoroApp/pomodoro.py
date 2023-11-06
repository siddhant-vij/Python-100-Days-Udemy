from tkinter import *

IMAGE_BG = "./PomodoroApp/tomato.png"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


reps = 0
timer = None


# ---------------------TIMER MECHANISM-------------------
def startTimer():
    global reps
    reps += 1
    if reps % 8 == 0:
        countDown(LONG_BREAK_MIN*60)
        timerLabel.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countDown(SHORT_BREAK_MIN*60)
        timerLabel.config(text="Break", fg=PINK)
    else:
        countDown(WORK_MIN*60)
        timerLabel.config(text="Work", fg=GREEN)


def resetTimer():
    window.after_cancel(timer)
    canvas.itemconfig(timerText, text="00:00")
    timerLabel.config(text="Timer", fg=GREEN)
    checkmarkLabel.config(text="")
    global reps
    reps = 0


# ---------------------COUNTDOWN MECHANISM-------------------
def countDown(count):
    countMin = int(count / 60)
    countSec = count % 60
    if countSec < 10:
        countSec = f"0{countSec}"
    if countMin < 10:
        countMin = f"0{countMin}"

    canvas.itemconfig(timerText, text=f"{countMin}:{countSec}")
    if count > 0:
        global timer
        timer = window.after(1000, countDown, count - 1)
    else:
        startTimer()
        marks = ""
        workSessions = int(reps / 2)
        for _ in range(workSessions):
            marks += "✔"
        checkmarkLabel.config(text=marks)


# ---------------------UI SETUP-------------------
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# Place Image & Timer on Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImg = PhotoImage(file=IMAGE_BG)
canvas.create_image(100, 112, image=tomatoImg)
timerText = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


# Pomodoro Timer Title on Canvas
timerLabel = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timerLabel.grid(row=0, column=1)


# Start & Reset Buttons
startButton = Button(text="Start", font=(FONT_NAME, 15), highlightthickness=0, command=startTimer)
startButton.grid(row=2, column=0)
resetButton = Button(text="Reset", font=(FONT_NAME, 15), highlightthickness=0, command=resetTimer)
resetButton.grid(row=2, column=2)


# Checkmark Label
checkmarkLabel = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
checkmarkLabel.grid(row=3, column=1)


window.mainloop()
