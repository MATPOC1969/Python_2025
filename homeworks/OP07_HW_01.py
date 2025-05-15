import tkinter as tk

def hello():
    name_user = entry.get()
    label.config(text=f"Привет, {name_user}!")

root = tk.Tk()
root.title("Напиши свое имя")

label = tk.Label(root, text="Как тебя зовут?")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Привет!", command=hello)
button.pack()

root.mainloop()
