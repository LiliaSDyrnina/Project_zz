from tkinter import *
import tkinter as tk


root = tk.Tk()
root.title("Ошибка")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


window_width = 500
window_height = 500
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

label1 = tk.Label(root, text="Такого человека нет в нашей группе!",font="Courier 15",bg="red")
label1.place(x=30, y=100)
   
def buttonback_click():

    
    root.destroy()
    import form

buttonback = tk.Button(root, text="На главную",font="Courier 10",command=buttonback_click)
buttonback.place(x=355, y=180)


root.mainloop()    

