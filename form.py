from tkinter import *
import tkinter as tk


root = tk.Tk()
root.title("Добро пожаловать в КНТ-6")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


window_width = 500
window_height = 500
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.mainloop()    

label1 = tk.Label(root, text="Привет!",font="Courier 20",bg="pink")
label1.place(x=100, y=100)
label2 = tk.Label(root, text="Введи дату своего рождения",font="Courier 15",bg="pink")
label2.place(x=150, y=150)
entry=tk.Entry(root,font=" 10")
entry.place(x=150,y=180)

button1 = tk.Button(root, text="ok",font="Courier 10",command=button1_click)
button1.place(x=355, y=180)
