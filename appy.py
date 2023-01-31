import random
import string
import tkinter as tk
from tkinter import Entry, Label, Button


def generate_password():
    characters = "-" + string.ascii_letters + "-" + "@" + string.digits + "-"
    length = entry.get()
    password = ''.join(random.choice(characters) for i in range(int(length)))
    label.config(text=f"Your password gereta: {password}")


root = tk.Tk()
root.title("Password Generator")

label = Label(root, text="")
label.pack()

entry = Entry(root, width=50)
entry.pack()
entry.insert(0, 20)

button = Button(root, text="Generate", command=generate_password)
button.pack()

root.mainloop()
