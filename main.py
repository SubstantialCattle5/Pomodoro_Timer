# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 25 * 60
SHORT_BREAK_SEC = 5 * 60
LONG_BREAK_SEC = 20 * 60
time = None
import tkinter, math
from PIL import ImageTk, Image


# ---------------------------- TIMER RESET ------------------------------- #

def timer_reset():
    # try-except created in order to skip the first error
    try:
        global i, reps, time
        reps, i = 0, 1
        # Stop the timer
        root.after_cancel(time)
        # Remove the checkmark
        mark.config(text='')
    except:
        print('first')


# ---------------------------- TIMER MECHANISM ------------------------------- #
reps = 0  # for the breaks
i = 1  # for the checkboxes


# For starting the timer and removing all the check
def start():
    timer_reset()
    timer_mech()


def timer_mech():
    global reps, i

    # to reset the check marks
    if reps == 0: mark.config(text='')

    reps += 1

    if reps % 8 == 0:

        # long break
        final_countdown(4)
        print('Long break')
        # Changing the title to Break
        heading.config(text='Break', fg=GREEN)
        # Resetting the check marks
        i = 1
        mark.config(text='Congratulations!')

    elif reps % 2 == 0:
        final_countdown(2)
        print('Short break')  # short break
        heading.config(text='Break', fg=PINK)
    else:
        final_countdown(6)
        print('Work')  # work
        heading.config(text='Work', fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def final_countdown(count):
    global i, time
    # Time format calc
    hrs = math.floor(count / 60)
    min = count - hrs * 60

    # formatting the time
    if len(str(hrs)) == 1:
        if len(str(min)) == 1:
            time_format = f'0{hrs}:0{min}'
        else:
            time_format = f'0{hrs}:{min}'
    else:
        time_format = f'{hrs} : {min}'

    # Updating the time
    canvas.itemconfig(timer, text=time_format)

    # calculating the time limit
    if count > 0:
        # calling the countdown after every second
        time = root.after(1000, final_countdown, count - 1)
    if count == 0:
        # to increase the tick mark and start the timer again
        timer_mech()
        mark.config(text=check_mark * i)
        i += 1


# ---------------------------- UI SETUP ------------------------------- #

root = tkinter.Tk()
root.title('Pomodoro Timer')
root.config(padx=80, pady=80, bg=YELLOW)

# heading
heading = tkinter.Label(text='Timer', font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
heading.grid(row=0, column=2)

# Wallpaper + Timer
canvas = tkinter.Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
# Creating the image file
img = ImageTk.PhotoImage(Image.open("tomato.png"))
canvas.create_image(100, 111, image=img)
# Creating the text file
timer = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=2, column=2)

# Start Button
start_button = tkinter.Button(text='Start', command=lambda: start())
start_button.config(width=10)
start_button.grid(row=3, column=1)

# Stop Button
stop_button = tkinter.Button(text='Stop', command=lambda: timer_reset())
stop_button.config(width=10)
stop_button.grid(row=3, column=3)

# Check mark
check_mark = '✓'
mark = tkinter.Label(text='', bg=YELLOW, font=(FONT_NAME, 18))
mark.grid(row=3, column=2)

root.mainloop()
