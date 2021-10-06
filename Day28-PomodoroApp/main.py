from tkinter import * 
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def restart_timer():
    window.after_cancel(timer)
    global reps
    reps = 0

    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    checkmark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 2 == 1:
        countdown(60*WORK_MIN)
        label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36, "bold"))
    elif reps == 8:
        countdown(60*LONG_BREAK_MIN)
        label.config(text="Long break", fg=RED, bg=YELLOW, font=(FONT_NAME, 36, "bold"))
    else:
        countdown(60*SHORT_BREAK_MIN)
        label.config(text="Short break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 36, "bold"))
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer

    min = math.floor(count/60)
    sec = count % 60
    if sec == 0:
        sec = "00"
    elif sec < 10:
        sec = "0" + str(sec)
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        new_text = ""
        for _ in range(math.floor(reps/2)):
            new_text += CHECKMARK
        checkmark.config(text=new_text)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=60, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36, "bold"))
label.grid(row=1, column=2)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=3, column=1)

restart = Button(text="Restart", highlightthickness=0, command=restart_timer)
restart.grid(row=3, column=3)

checkmark = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 14, "bold"))
checkmark.grid(row=4,column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="C:/Users/Olivera/Documents/Python learning/Day28-PomodoroApp/tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

window.mainloop()
