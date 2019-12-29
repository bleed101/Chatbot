from tkinter import *
import random
from datetime import datetime
root=Tk()
root.title('Chatbot')
heading=Label(root,text="Let's Talk...!",font=('Comic Sans MS',30,'bold'),bg='#f7dc6f')
heading.pack()
frame=Frame(root)
scroll=Scrollbar(frame)
scroll.pack(side=RIGHT, fill=Y)

def center_window(w=500, h=400):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

center_window() 

a=Entry(root,width=30,bd=3)
lis=Listbox(frame,yscrollcommand=scroll.set,height=15,width=50,bg='#99a3a4')
def p():
    lis.insert(END,"                                                                   "+a.get())
    lis.insert(END,"\n")
    lis.yview(END)
    u=a.get()
    reply(u)


def reply(user):
    aiHi={1:'Hey!',2:'Hi,how can I a assist you.'}
    aiSet1={
        1:'Hi I am fine, how i can help you.',
        2:'Getting use to you  ',
        3:'I am D',
        4:'Sorry!, I can only perform 2 one digit number addition',
        5:'Sorry!, I can only perform 2 one digit number subtraction',
        7:'Sorry!, I can only perform 2 one digit number division',
        8:'Sorry!, I can only perform 2 one digit number multiplication',
        }
    aiSet1Values=list(aiSet1.values())

    userList={
        1:'hi',
        2:'Hi',
        3:'hi!',
        4:'Hi!',
        5:'hi sup',
        6:'Hi sup',
        7:'hi what are you doing',
        8:'what are you doing',
        9:'what is your name',
        10:'name',
        11:'time',
        12:'date',
    }
    userListValues=list(userList.values())
    if user in userListValues:
        index=userListValues.index(user)+1
    else:
        index=0
    if index>=1 and index<=4:
        # print(random.choice(aiHi.values()))
        lis.insert(END,random.choice(aiHi.values()))
    elif index==5 or index==6:
        lis.insert(END,aiSet1[1])
    elif index==7 or index==8:
        lis.insert(END,aiSet1[2])
    elif index==9 or index==10:
        lis.insert(END,aiSet1[3])
    elif index==11:
        time=datetime.now()
        str_time=time.strftime("%H:%M:%S")
        lis.insert(END,"it's : "+str_time)
    elif index==12:
        date=datetime.now()
        str_date=date.strftime("%d/%m/%Y")
        lis.insert(END,"Today is : "+str_date) 
    elif user[1]=='+':
        lis.insert(END,add(user))
    elif user[1]=='-':
        lis.insert(END,sub(user))
    elif user[1]=='/':
        lis.insert(END,div(user))
    elif user[1]=='*':
        lis.insert(END,mul(user))
    else:
        lis.insert(END,'Oooops!')

def add(user):
    if len(user)==3:
        a=int(user[0])
        b=int(user[2])
        return a+b
    

def sub(user):
    if len(user)==3:
        a=int(user[0])
        b=int(user[2])
        return a-b
    

def div(user):
    if len(user)==3:
        a=float(user[0])
        b=float(user[2])
        rd=round(a/b,2)
        return rd
    

def mul(user):
    if len(user)==3:
        a=int(user[0])
        b=int(user[2])
        return a*b


lis.pack()
scroll.config(command=lis.yview)
a.place(x=40,y=360)
submit = Button(root, text ="Submit",command=p)
submit.place(x=395,y=360,height=30,width=65)
frame.pack()
root.configure(background='#f7dc6f')
root.mainloop()