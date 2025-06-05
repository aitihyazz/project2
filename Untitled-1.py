from tkinter import *

window = Tk()
window.geometry('400x400')
window.title("Getting started with widgets")


lb1 = Label(text="Multiplication", fg="white", bg="navy blue", height=2, width=30)
lb2 = Label(text="First number", fg="white", bg="blue", height=2, width=20)
lb3 = Label(text="Second number", fg="white", bg="blue", height=2, width=20)


entry1 = Entry()
entry2 = Entry()

result_label = Label(text="Result will appear here", bg="lightgray", width=30)

def multi():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")


btn = Button(text="Multiply", command=multi, bg="green", fg="white", width=20)


lb1.pack(pady=10)
lb2.pack()
entry1.pack(pady=5)
lb3.pack()
entry2.pack(pady=5)
btn.pack(pady=10)
result_label.pack(pady=10)

window.mainloop()
