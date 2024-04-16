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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_title.config(text="Timer" ,fg=GREEN)
    check_marks.config(text="", fg=GREEN,bg=YELLOW)
    global reps
    reps = 0

    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def change_title(time):
    if time == LONG_BREAK_MIN:
        timer_title.config(text="Long Break", fg=RED)

    elif time == SHORT_BREAK_MIN:
        timer_title.config(text="Short Break", fg=PINK)
    else:
        timer_title.config(text="Working time" ,fg=GREEN) 



def start_timer():
    work_sec = WORK_MIN * 60 
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    global reps
    reps+=1
    if reps % 8 == 0:
        change_title(LONG_BREAK_MIN)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        change_title(SHORT_BREAK_MIN)
        count_down(short_break_sec)
    else: 
         change_title(WORK_MIN)  
         count_down(work_sec)  
    
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    minutes = math.floor(count / 60)
    secondes = count % 60
    if secondes < 10:
        secondes = f"0{secondes}"
        
    canvas.itemconfig(timer_text,text=f"{minutes}:{secondes}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checkmark = ""
        if reps % 2 == 0:
            sessions = reps / 2
            for _ in range(sessions):
                checkmark+="✔"
            check_marks.config(text=checkmark, fg=GREEN,bg=YELLOW)



# ---------------------------- UI SETUP ------------------------------- #
from  tkinter import *
window = Tk()
window.config(padx=100, pady=50,bg=YELLOW)
window.title("Pomodoro")




timer_title = Label(text="Timer", fg="green",bg=YELLOW, font=(FONT_NAME, 50))
timer_title.grid(row=0,column=1)


canvas = Canvas(width=210, height=224, bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(103,112 ,image=tomato_img)
timer_text = canvas.create_text(103, 130,text="00:00" ,fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1 ,column=1)


start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)



reset_button = Button(text="Reset",highlightthickness=0 ,command=reset_timer)
reset_button.grid(row=2,column=2)

check_marks = Label()
check_marks.grid(row=3,column=1)

window.mainloop()