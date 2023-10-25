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
print(dates)
'''if data in dates: 
    if sex=='ж':
        for i in range(len(dates)):
            if dates[i]==data:
                index=i
                break
    if sex=='м':
        for i in range(len(dates)):
            if dates[i]==data:
                index=i
    label1=''.join(('Привет, ',names[index],'!'))
    label2=''.join(('Твой знак зодиака: ', signs[index]))
    label3=''.join(('Твои личностные качества: ', captions[index]))
    label4=''.join(('В нашей группе у тебя ты cможешь построить доверительные отношения с ', connections[index]))'''



        
