from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = ""
timer = None
work_sec = WORK_MIN *60
short_break_sec = SHORT_BREAK_MIN *60
long_break_sec = LONG_BREAK_MIN *60
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 ==0:
        countdown(long_break_sec)
        timer_label.config(text="Long Break",fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Short Break",fg=PINK)
    else:
        countdown(work_sec)
        print(reps)
        timer_label.config(text="Work",fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global checkmarks
    minutes = math.floor(count/60)
    seconds = round(count % 60,2)
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000,countdown,count-1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            checkmarks += "✔"
            checkmark_label.config(text=checkmarks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady=50, bg=YELLOW)


canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image)
timer_text = canvas.create_text(100,130,text=f"00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

#fg to color the label
#✔


reset_button = Button(text="Reset",command=timer_reset)
timer_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,35,"bold"),bg=YELLOW)
checkmark_label = Label(text= checkmarks,fg=GREEN,bg=YELLOW)
start_button = Button(text="Start",command=start_timer)

timer_label.grid(column=1,row=0)
start_button.grid(column=0,row=2)
reset_button.grid(column=2,row=2)
checkmark_label.grid(column=1,row=3)
window.mainloop()