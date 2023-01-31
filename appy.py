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
root.geometry("500x400+100+100")

label = Label(root, text="")
label.pack(side="top", fill="both", expand=True, anchor="center")

entry = Entry(root, width=50)
entry.pack(side="top", fill="both", expand=True, anchor="center")
entry.insert(0, 20)

button = Button(root, text="Generate", command=generate_password)
button.pack(side="bottom", fill="both", expand=True, anchor="center", pady=25, padx=25)

root.mainloop()

