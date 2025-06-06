from tkinter import *

window = Tk()
window.geometry('400x400')
window.title("Age calulator")


lb1 = Label(text="Passord strenght checker", fg="white", bg="navy blue", height=2, width=30)
lb2 = Label(text="Enter your password", fg="white", bg="blue", height=2, width=20)

passen = Entry()

result_label = Label(text="Your age will appear here", bg="lightgray", width=30)
def checker():
    password = passen.get()
    if len(password) >= 12:
        result_label.config(text="Strong Password", bg="green")
    elif len(password) >= 8:
        result_label.config(text="Moderate Password", bg="orange")
    else:
        result_label.config(text="Weak Password", bg="red")

btn = Button(text="Check Password", command=checker, bg="green", fg="white", width=20)


lb1.pack(pady=10)
lb2.pack()
passen.pack(pady=5)
btn.pack(pady=10)
result_label.pack(pady=10)


window.mainloop()