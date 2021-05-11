from tkinter import *

window = Tk()

# question label and adjusting placement
first_no = Label(window, text="Enter First Number")
first_no.grid(column=1, row=1)

first_no_entry = Entry(window)
first_no_entry.grid(column=2, row=1)

second_no = Label(window, text="Enter Second Number")
second_no.grid(column=1, row=2)

second_no_entry = Entry(window)
second_no_entry.grid(column=2, row=2)

answer_label = Label(window, text="Your Answer")
answer_label.grid(column=1, row=3)

answer_entry = Entry(window, state="readonly")
answer_entry.grid(column=2, row=3)


def add_two_numbers():
    result = sum(int(i.get()) for i in (first_no_entry, second_no_entry))
    answer_entry.config(state="normal")
    answer_entry.insert(0, result)
    answer_entry.config(state="readonly")


def clear():
    first_no_entry.delete(0, END)
    second_no_entry.delete(0, END)
    answer_entry.config(state="normal")
    answer_entry.delete(0, END)
    answer_entry.config(state="readonly")

add = Button(window, text="Add", command=add_two_numbers)
add.grid(column=1, row=4)

clear = Button(window, text="Clear", command=clear)
clear.grid(column=2, row=4)

exit_button = Button(window, text="Exit", command="exit")
exit_button.grid(column=3, row=4)

mainloop()
