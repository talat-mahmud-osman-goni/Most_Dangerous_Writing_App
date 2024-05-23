from tkinter import *

FONT_NAME = 'Courier'
session_time_list = ['1 Minutes', '2 Minutes', '3 Minutes', '4 Minutes', '5 Minutes']
update_timer = None
clear_timer = None
remaining_time = 0
session_minutes = None


def handle_key_press(event):
    global clear_timer
    if clear_timer:
        window.after_cancel(clear_timer)

    text = typing_text.get(1.0, "end-1c")
    word_count.config(text=f"{len(text.split())} Words")

    clear_timer = window.after(5000, clear_text)


def clear_text():
    typing_text.delete(1.0, "end-1c")
    word_count.config(text="0 Words")


def start_session():
    typing_text.config(state="normal")
    global remaining_time, session_minutes
    session_minutes = int(value_inside.get().split()[0])
    remaining_time = session_minutes * 60
    update_timer_display()


def update_timer_display():
    global remaining_time, update_timer
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    timer_label.config(text=f"{minutes:02}:{seconds:02}")
    time = int(value_inside.get().split()[0])

    if remaining_time > 0:
        remaining_time -= 1
        update_timer = window.after(1000, update_timer_display)
    else:
        words = typing_text.get(1.0, "end-1c")
        words_count = len(words.split())

        typing_text.delete(1.0, "end-1c")
        typing_text.insert(INSERT, f"Your Typing Speed is {words_count/time} words per minutes.")
        typing_text.config(fg='red', state="disabled")


window = Tk()
window.title('Most Dangerous Writing App')
window.config(padx=20, pady=20, bg='#987dbd')

Label(text='Most Dangerous Writing App', bg='#987dbd', fg='white', font=(FONT_NAME, 35, 'bold'), anchor="nw").grid(
    row=0, column=1, columnspan=2)

# -------Session Length Dropdown----
Label(text='Session Length: ', bg='#987dbd', fg='white', font=(FONT_NAME, 12), padx=150).grid(sticky=W, row=1, column=0,
                                                                                              columnspan=2)
value_inside = StringVar()
value_inside.set('1 Minutes')

dropdown = OptionMenu(window, value_inside, *session_time_list)
dropdown.config(width=10, padx=5, pady=5, bg='#987dbd', fg='white', highlightthickness=0)
dropdown.grid(row=1, column=1, columnspan=2)

# -------Start Button-----------
start_button = Button(text="Start Session", command=start_session, bg='#987dbd', fg='white', font=(FONT_NAME, 12))
start_button.grid(row=1, column=3, padx=10)

# -------Typing Textbox-----------
typing_text = Text(width=50, height=10, bg='#401e6e', fg="white", highlightthickness=2, font=("Arial", 24))
typing_text.grid(row=2, column=1, columnspan=3)
typing_text.bind("<Key>", handle_key_press)
typing_text.config(state="disabled")

# ---------Word Count----
word_count = Label(text='0 Words', bg='#987dbd', fg='white', font=(FONT_NAME, 12), padx=250)
word_count.grid(sticky=W, row=3, column=1, columnspan=2)

# ---------Timer Label----
timer_label = Label(text="00:00", bg='#987dbd', fg='white', font=(FONT_NAME, 12))
timer_label.grid(row=3, column=3, padx=10)

window.mainloop()
