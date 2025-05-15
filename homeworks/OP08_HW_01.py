import tkinter as tk
root = tk.Tk()
root.title("Список задач")
root.configure(background="aquamarine1")

text1 = tk.Label(root, text="Новая задача",bg="CadetBlue")
text1.grid(row=0,column=1)

task_entry = tk.Entry(root,width=30)
task_entry.grid(row=1,column=1)

button_task_new=tk.Button(root,text="Добавить задачу")
button_task_new.grid(row=2,column=0)
button_task_work=tk.Button(root,text="Взять в работу")
button_task_work.grid(row=2,column=1)
button_task_end=tk.Button(root,text="Завершить")
button_task_end.grid(row=2,column=2)

list_task_new=tk.Listbox(root)
list_task_new.grid(row=3,column=0)
list_task_work=tk.Listbox(root)
list_task_work.grid(row=3,column=1)
list_task_end=tk.Listbox(root)
list_task_end.grid(row=3,column=2)
root.mainloop()
