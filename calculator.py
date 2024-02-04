from tkinter import *
from tkinter import messagebox


root=Tk()

root.title("calculator")

root.geometry("180x230+480+250")

root.resizable(0,0)

enttext=StringVar()

ent=Entry(root,width=28,textvariable=enttext)
ent.grid(row=0,column=0,columnspan=4)

def calculator():
    try:
        khoroji=eval(enttext.get())
        enttext.set(khoroji)
    except:
        ent.delete(0,END)
        messagebox.showerror("Error")


but0=Button(root,text="0",width=11,height=2,command=lambda:ent.insert(END,"0"))
but0.grid(row=4,column=0,columnspan=2)

but1=Button(root,text="1",width=5,height=2,command=lambda:ent.insert(END,"1"))
but1.grid(row=3,column=2)

but2=Button(root,text="2",width=5,height=2,command=lambda:ent.insert(END,"2"))
but2.grid(row=3,column=1)

but3=Button(root,text="3",width=5,height=2,command=lambda:ent.insert(END,"3"))
but3.grid(row=3,column=0)

but4=Button(root,text="4",width=5,height=2,command=lambda:ent.insert(END,"4"))
but4.grid(row=2,column=0)

but5=Button(root,text="5",width=5,height=2,command=lambda:ent.insert(END,"5"))
but5.grid(row=2,column=1)

but6=Button(root,text="6",width=5,height=2,command=lambda:ent.insert(END,"6"))
but6.grid(row=2,column=2)

but7=Button(root,text="7",width=5,height=2,command=lambda:ent.insert(END,"7"))
but7.grid(row=1,column=0)

but8=Button(root,text="8",width=5,height=2,command=lambda:ent.insert(END,"8"))
but8.grid(row=1,column=1)

but9=Button(root,text="9",width=5,height=2,command=lambda:ent.insert(END,"9"))
but9.grid(row=1,column=2)

div=Button(root,text="\U000000F7",width=5,height=2,command=lambda:ent.insert(END,"/"))
div.grid(row=1,column=3)

mul=Button(root,text="\U000000D7",width=5,height=2,command=lambda:ent.insert(END,"*"))
mul.grid(row=2,column=3)

plus=Button(root,text="+",width=5,height=2,command=lambda:ent.insert(END,"+"))
plus.grid(row=4,column=2)

sub=Button(root,text="-",width=5,height=2,command=lambda:ent.insert(END,"-"))
sub.grid(row=3,column=3)

equ=Button(root,text="=",width=5,height=2,command=calculator)
equ.grid(row=4,column=3)

fl=Button(root,text=".",width=5,height=2,command=lambda:ent.insert(END,"."))
fl.grid(row=5,column=0,)


bclear=Button(root,text="AC",width=18,height=2,command=lambda:ent.delete(0,END))
bclear.grid(row=5,column=1,columnspan=3)

root.mainloop()