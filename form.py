<<<<<<< HEAD
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

label1 = tk.Label(root, text="Привет!",font="Courier 20",bg="pink")
label1.place(x=100, y=100)
label2 = tk.Label(root, text="Введи дату своего рождения",font="Courier 15",bg="pink")
label2.place(x=150, y=150)
entry=tk.Entry(root,font="Courier 13")
entry.place(x=150,y=180)

def button1_click():
    date=entry.get()
    label3 = tk.Label(root, text="Вы",font="Courier 15",bg="pink")
    label3.place(x=150, y=220)
    buttonw = tk.Button(root, text="женщина",font="Courier 10",bg="pink",command=buttonw_click)
    buttonw.place(x=210, y=220)
    buttonm = tk.Button(root, text="мужчина",font="Courier 10",bg="blue",command=buttonm_click)
    buttonm.place(x=290, y=220)
    
button1 = tk.Button(root, text="ok",font="Courier 10",command=button1_click)
button1.place(x=355, y=180)
def go_click():
    parameters=open('info.txt').readlines()
    dates=[]
    sexes=[]
    names=[]
    signs=[]
    captions=[]
    connections=[]
    for i in range(0,len(parameters)):
        if i%6==0:
            dates+=[''.join(parameters[i][0:-1:])]
        if i%6==1:
            sexes+=[''.join(parameters[i][0:-1:])]
        if i%6==2:
            names+=[''.join(parameters[i][0:-1:])]
        if i%6==3:
            signs+=[''.join(parameters[i][0:-1:])]
        if i%6==4:
            captions+=[''.join(parameters[i][0:-1:])]
        if i%6==5:
            connections+=[''.join(parameters[i][0:-1:])]
    if data in dates: 
        if sex=='ж':
            for i in range(len(dates)):
                if dates[i]==data:
                    index=i
                    break
        if sex=='м':
            for i in range(len(dates)):
                if dates[i]==data:
                    index=i
        root.destroy()
        import good
        label1=''.join(('Привет, ',names[index],'!'))
        label2=''.join(('Твой знак зодиака: ', signs[index]))
        label3=''.join(('Твои личностные качества: ', captions[index]))
        label4=''.join(('В нашей группе у тебя ты cможешь построить доверительные отношения с ', connections[index]))
    else:
        root.destroy()
        import bug



def buttonw_click():
    sex='ж'
    button_go = tk.Button(root, text="Рассчитать",font="Courier 15",command=go_click)
    button_go.place(x=100, y=266)

    
def buttonm_click():
    sex='м'
    button_go = tk.Button(root, text="Рассчитать",font="Courier 15",command=go_click)
    button_go.place(x=100, y=266)



root.mainloop()    
