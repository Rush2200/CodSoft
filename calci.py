from tkinter import *
main=Tk()
main.title("Calculator")
main.geometry("300x500")
main.maxsize(width=300,height=500)

calculation="" 

f1=Frame(main,borderwidth=5)
f1.pack(side=LEFT)

e1=Text(f1,height=2, width=15, font=("Arial", 24))
e1.grid(row=0,column=1,columnspan=4)

def add(symbol): 
     global calculation 
     calculation += str(symbol) 
     e1.delete(1.0,"end") 
     e1.insert(1.0,calculation)

def total(): 
     global calculation 
     try: 
         calculation = str(eval(calculation)) 
         e1.delete(1.0,"end") 
         e1.insert(1.0, calculation) 
     except: 
         clear() 
         e1.insert(1.0,"error")

def clear(): 
     global calculation 
     calculation ="" 
     e1.delete(1.0,"end")

l1=Label(f1,text="")
l1.grid(row=1,column=0,columnspan=4)

btc=Button(f1,text="C",width=10,height=3,command=clear)
btc.grid(row=2,column=1,columnspan=2)
btrem=Button(f1,text="%",width=5,height=3,command=lambda: add("%"))
btrem.grid(row=2,column=3)
btdiv=Button(f1,text="/",width=5,height=3,command=lambda: add("/"))
btdiv.grid(row=2,column=4)

l2=Label(f1,text="")
l2.grid(row=3,column=0,columnspan=4)

bt7=Button(f1,text="7",width=5,height=3,command=lambda: add(7))
bt7.grid(row=4,column=1)
bt8=Button(f1,text="8",width=5,height=3,command=lambda: add(8))
bt8.grid(row=4,column=2)
bt9=Button(f1,text="9",width=5,height=3,command=lambda: add(9))
bt9.grid(row=4,column=3)
btmul=Button(f1,text="*",width=5,height=3,command=lambda: add("*"))
btmul.grid(row=4,column=4)

l3=Label(f1,text="")
l3.grid(row=5,column=0,columnspan=4)

bt4=Button(f1,text="4",width=5,height=3,command=lambda: add(4))
bt4.grid(row=6,column=1)
bt5=Button(f1,text="5",width=5,height=3,command=lambda: add(5))
bt5.grid(row=6,column=2)
bt6=Button(f1,text="6",width=5,height=3,command=lambda: add(6))
bt6.grid(row=6,column=3)
btsub=Button(f1,text="-",width=5,height=3,command=lambda: add("-"))
btsub.grid(row=6,column=4)

l4=Label(f1,text="")
l4.grid(row=7,column=0,columnspan=4)

bt1=Button(f1,text=1,width=5,height=3,command=lambda: add(1))
bt1.grid(row=8,column=1)
bt2=Button(f1,text="2",width=5,height=3,command=lambda: add(2))
bt2.grid(row=8,column=2)
bt3=Button(f1,text="3",width=5,height=3,command=lambda: add(3))
bt3.grid(row=8,column=3)
btadd=Button(f1,text="+",width=5,height=3,command=lambda: add("+"))
btadd.grid(row=8,column=4)

l5=Label(f1,text="")
l5.grid(row=9,column=0,columnspan=4)

bt0=Button(f1,text="0",width=5,height=3,command=lambda: add(0))
bt0.grid(row=10,column=1)
btdot=Button(f1,text=".",width=5,height=3,command=lambda: add("."))
btdot.grid(row=10,column=2)
btres=Button(f1,text="=",width=15,height=3,command=total)
btres.grid(row=10,column=3,columnspan=2)


main.mainloop()