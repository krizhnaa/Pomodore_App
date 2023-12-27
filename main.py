from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodore Timer")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label()
label.config(text="Timer", font=(FONT_NAME, 28, "bold"), bg=YELLOW, foreground=GREEN)
label.grid(row=0, column=1)

label1 = Label()
label1.config(text="✓", font=(FONT_NAME, 12, "bold"), bg=YELLOW, foreground=GREEN)
label1.grid(row=3, column=1)

start = Button()
start.config(text="Start")
start.grid(row=2, column=0)

reset = Button()
reset.config(text="Reset")
reset.grid(row=2, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tom_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tom_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)







window.mainloop()