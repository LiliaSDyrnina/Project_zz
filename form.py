from tkinter import *
import tkinter as tk
from textwrap import wrap

root = tk.Tk()
root.title("Добро пожаловать в КНТ-6")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.config(cursor="sailboat")

root.configure(bg='white')

img = PhotoImage(file="2.png")
label = Label(root, image=img)
label.place(x=10,y=10)
window_width = 500
window_height = 500
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

label1 = tk.Label(root, text="Здравствуй!",font="TkHeadingFont 17",bg="#c8b2d8")
label1.place(x=100, y=100)
label2 = tk.Label(root, text="Введи дату рождения",font="Courier 15",bg="#c0c0c0")
label2.place(x=150, y=150)
entry=tk.Entry(root,font="Courier 13")
entry.place(x=150,y=180)



 
def button1_click():
    data=str(entry.get())
    label3 = tk.Label(root, text="Вы",font="Courier 19",bg="#c8b2d8")
    label3.place(x=150, y=220)
    buttonw = tk.Button(root, text="женщина",font="Courier 13",bg="#7299df",command=buttonw_click)
    buttonw.place(x=206, y=220)
    buttonm = tk.Button(root, text="мужчина",font="Courier 13",bg="#ec5679",command=buttonm_click)
    buttonm.place(x=295, y=220)
    return data
    
button1 = tk.Button(root, text="ok",font="Courier 10",bg="#c8b2d8", command=button1_click)
button1.place(x=355, y=180)
def buttonw_click():
    sex='ж'
    def go_click():
        parameters=open('info.txt','r',encoding='utf-8').readlines()
        dates=[]    
        data=(entry.get())        
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
            
            for widget in root.place_slaves():
                widget.place_forget()
            
            
            label1=''.join(('Привет, ',names[index],'!'))
            
            label_1 = tk.Label(root, text=label1,font="Courier 15",cursor="pencil",bg='white')            
            label_1.place(x=180, y=20)
            root.configure(bg='white')
            
                   

            
            labe1=''.join(('Привет, ',names[index],'!'))
            
            
            label2=''.join(('Твой знак зодиака: ', signs[index]))
            label_2 = tk.Label(root, text=label2,font="Courier 13",bg="#efdecd")
            label_2.place(x=10, y=70)
            
            
            
            label3_=''.join((captions[index]))
                    
            
            label_9 = tk.Label(root, text="Личностные качества: ",font="Courier 13",bg="#c0c0c0")
            label_9.place(x=10, y=110)
            label3=''.join(captions[index])
                        
            
            text=label3_
            label = Label(root, text=text,font="Courier 13",bg="white",anchor="e")
            label.place(x=10,y=140)       
            root.update()  

            width = label.winfo_width()

            if width > 475:
                char_width = width / len(text)
                wrapped_text = '\n'.join(wrap(text, int(475 / char_width)))
                label['text'] = wrapped_text
            label4_=''.join((connections[index]))
            label_10 = tk.Label(root, text="У тебя хорошая совместимость с этими людьми:",font="Courier 13",bg="#b2cde8")
            label_10.place(x=10, y=310)
                
            text=label4_
            label = Label(root, text=text,font="Courier 12",bg="white",cursor="gumby")
            label.place(x=10,y=335)       
            root.update()  

            width = label.winfo_width()

            if width > 475:
                char_width = width / len(text)
                wrapped_text = '\n'.join(wrap(text, int(475/ char_width)))
                label['text'] = wrapped_text
            
          
           
        else:
            
            root.destroy()
            import bug


    button_go = tk.Button(root, text="Рассчитать",font="Courier 15",bg="#c8b2d8",command=go_click)
    button_go.place(x=100, y=266)
    

def buttonm_click():
    sex='м'
    def go_click():
        parameters=open('info.txt','r',encoding='utf-8').readlines()
        dates=[]    
        data=(entry.get())        
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
            
            for widget in root.place_slaves():
                widget.place_forget()
            
            
            label1=''.join(('Привет, ',names[index],'!'))
            
            label_1 = tk.Label(root, text=label1,font="Courier 15",cursor="pencil",bg='white')            
            label_1.place(x=20, y=20)
            root.configure(bg='white')
            
                   

            
            labe1=''.join(('Привет, ',names[index],'!'))
            
            
            label2=''.join(('Твой знак зодиака: ', signs[index]))
            label_2 = tk.Label(root, text=label2,font="Courier 13",bg="#efdecd")
            label_2.place(x=10, y=70)
            
            
            
            label3_=''.join((captions[index]))
                    
            
            label_9 = tk.Label(root, text="Личностные качества: ",font="Courier 13",bg="#c0c0c0")
            label_9.place(x=10, y=110)
            label3=''.join(captions[index])
                        
            
            text=label3_
            label = Label(root, text=text,font="Courier 13",bg="white",anchor="e")
            label.place(x=10,y=140)       
            root.update()  

            width = label.winfo_width()

            if width > 475:
                char_width = width / len(text)
                wrapped_text = '\n'.join(wrap(text, int(475 / char_width)))
                label['text'] = wrapped_text
            label4_=''.join((connections[index]))
            label_10 = tk.Label(root, text="У тебя хорошая совместимость с этими людьми:",font="Courier 13",bg="#b2cde8")
            label_10.place(x=10, y=300)
                
            text=label4_
            label = Label(root, text=text,font="Courier 12",bg="white",cursor="gumby")
            label.place(x=10,y=335)       
            root.update()  

            width = label.winfo_width()

            if width > 475:
                char_width = width / len(text)
                wrapped_text = '\n'.join(wrap(text, int(475/ char_width)))
                label['text'] = wrapped_text
            
          
           
        else:
            
            root.destroy()
            import bug


    button_go = tk.Button(root, text="Рассчитать",font="Courier 15",bg="#c8b2d8",command=go_click)
    button_go.place(x=100, y=266)
       
'''def buttonm_click():
    sex='м'    
    def go_click():
        parameters=open('info.txt').readlines()
        dates=[]      
        data=(entry.get())
        print(sex)
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
            for widget in root.place_slaves():
                widget.place_forget()
            
            
            label1=''.join(('Привет, ',names[index],'!'))
            
            label_1 = tk.Label(root, text=label1,font="Courier 15",cursor="pencil",bg='white')            
            label_1.place(x=180, y=20)
            root.configure(bg='white')
            
                   

            
            labe1=''.join(('Привет, ',names[index],'!'))
            
            
            label2=''.join(('Твой знак зодиака: ', signs[index]))
            label_2 = tk.Label(root, text=label2,font="Courier 13",bg="#efdecd")
            label_2.place(x=10, y=70)
            
            
            
            label3_=''.join((captions[index]))
                    
            
            label_9 = tk.Label(root, text="Личностные качества: ",font="Courier 13",bg="#c0c0c0")
            label_9.place(x=10, y=110)
            label3=''.join(captions[index])
                        
            
            text=label3_
            label = Label(root, text=text,font="Courier 10",bg="white",anchor="e")
            label.place(x=10,y=140)       
            root.update()  

            width = label.winfo_width()

            if width > 475:
                char_width = width / len(text)
                wrapped_text = '\n'.join(wrap(text, int(475 / char_width)))
                label['text'] = wrapped_text
            label4_=''.join((connections[index]))
            label_10 = tk.Label(root, text="У тебя хорошая совместимость с этими людьми:",font="Courier 13",bg="#b2cde8")
            label_10.place(x=10, y=375)
                
            text=label4_
            label = Label(root, text=text,font="Courier 12",bg="white",cursor="gumby")
            label.place(x=10,y=400)       
            root.update()  

            width = label.winfo_width()

            if width > 475:
                char_width = width / len(text)
                wrapped_text = '\n'.join(wrap(text, int(475/ char_width)))
                label['text'] = wrapped_text
            
          
           
        else:
            
            root.destroy()
            import bug


    button_go = tk.Button(root, text="Рассчитать",font="Courier 15",bg="#c8b2d8",command=go_click)
    button_go.place(x=100, y=266)'''
    






root.mainloop()    

