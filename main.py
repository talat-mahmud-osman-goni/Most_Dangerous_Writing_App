from tkinter import *
import threading

FONT_NAME = 'Courier'
session_time_list = ['1 Minutes', '2 Minutes', '3 Minutes', '4 Minutes', '5 Minutes']
start_session = False

text = ""
update_timer = None


def handle_key_press(event):
    global text, update_timer, start_session
    start_session = True
    session()
    if update_timer:
        window.after_cancel(update_timer)

    text = typing_text.get(1.0, "end-1c")
    word_count.config(text=f"{len(text.split())} Words")

    update_timer = window.after(5000, clear_text)

    if not start_session:
        threading.Thread(target=count_time).start()
        start_session = True


def clear_text():
    typing_text.delete(1.0, "end-1c")
    word_count.config(text=f"0 Words")


def count_time(session_time):
    session_time = int(("{}".format(value_inside.get()))[0])*60
    if session_time > -1:
        window.after(1000, count_time, session_time - 1)
    else:
        typing_text.config(state="disabled")


def session():
    while start_session:
        session_time = int(("{}".format(value_inside.get()))[0])
        window.after(session_time*60000)  # begin updates


window = Tk()
window.title('Most Dangerous Writing App')
window.config(padx=20, pady=20, bg='#987dbd')

Label(text='Most Dangerous Writing App', bg='#987dbd', fg='white', font=(FONT_NAME, 35, 'bold'), anchor="nw").grid(
    row=0, column=1, columnspan=2)

# -------Session Length Dropdown----
Label(text='Session Length: ', bg='#987dbd', fg='white', font=(FONT_NAME, 12), padx=250).grid(sticky=W, row=1, column=0,
                                                                                              columnspan=2)
value_inside = StringVar()
value_inside.set('1 Minutes')

dropdown = OptionMenu(window, value_inside, *session_time_list)
dropdown.config(width=10, padx=5, pady=5, bg='#987dbd', fg='white', highlightthickness=0)
dropdown.grid(row=1, column=1, columnspan=2)

# -------Typing Textbox-----------
typing_text = Text(width=50, height=10, bg='#401e6e', fg="white", highlightthickness=2, font=("Arial", 24))
typing_text.grid(row=2, column=1, columnspan=2)
typing_text.bind("<Key>", handle_key_press)

# ---------Word Count----
word_count = (Label(text='0 Words', bg='#987dbd', fg='white', font=(FONT_NAME, 12), padx=250))
word_count.grid(sticky=W, row=3, column=1, )


window.mainloop()
