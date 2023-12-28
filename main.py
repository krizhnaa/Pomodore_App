from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 20
x_axis = 80
session = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def resett():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label1.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global session
    global x_axis

    session+=1
    if session % 8 == 0:
        label1.config(text="✓", font=(FONT_NAME, 12, "bold"), bg=YELLOW, foreground=GREEN)
        label1.place(x=x_axis, y=300)
        x_axis += 20
        count_down(LONG_BREAK_MIN)
    elif session % 2 == 0:
        label1.config(text="✓", font=(FONT_NAME, 12, "bold"), bg=YELLOW, foreground=GREEN)
        label1.place(x=x_axis, y=300)
        x_axis+=20
        count_down(SHORT_BREAK_MIN)
    else:
        count_down(WORK_MIN)


def short_break():
    count_down(SHORT_BREAK_MIN)


def long_break():
    count_down(LONG_BREAK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min = int(count/60)
    int_sec = count/60
    sec = int((int_sec - min) * 60)
    if sec == 0:
        sec = "00"
    elif sec <= 9:
        sec = "0" + f"{sec}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodore Timer")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label()
label.config(text="Timer", font=(FONT_NAME, 28, "bold"), bg=YELLOW, foreground=GREEN)
label.grid(row=0, column=1)

label1 = Label()

start = Button()
start.config(text="Start", command=start_timer)
start.grid(row=2, column=0)

reset = Button()
reset.config(text="Reset", command=resett)
reset.grid(row=2, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tom_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tom_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)





window.mainloop()