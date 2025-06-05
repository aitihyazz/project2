from tkinter import *
from datetime import date
window = Tk()
window.geometry('400x400')
window.title("Age calulator")


lb1 = Label(text="Age calculator", fg="white", bg="navy blue", height=2, width=30)
lb2 = Label(text="date", fg="white", bg="blue", height=2, width=20)
lb3 = Label(text="month", fg="white", bg="blue", height=2, width=20)
lb4 = Label(text="year", fg="white", bg="blue", height=2, width=20)


entry_day = Entry()
entry_month = Entry()
entry_year = Entry()

result_label = Label(text="Your age will appear here", bg="lightgray", width=30)
def calculateage():
    day = int(entry_day.get())
    month = int(entry_month.get())
    year = int(entry_year.get())
    birth_date = date(year, month, day)
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    result_label.config(text=f"You are {age} years old")



btn = Button(text="Calculate Age", command=calculateage, bg="green", fg="white", width=20)


lb1.pack(pady=10)
lb2.pack()
entry_day.pack(pady=5)
lb3.pack()
entry_month.pack(pady=5)
lb4.pack()
entry_year.pack(pady=5)
btn.pack(pady=10)
result_label.pack(pady=10)


window.mainloop()