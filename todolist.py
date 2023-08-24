from tkinter import *
main=Tk()
main.title("ToDo List")
main.minsize(width=500,height=600)

f1=Frame(main,bg="green").pack()
l1=Label(f1,text="ToDo List",font=("serif",30),bg="green").place(x=0,y=60)

f2=Frame(main,bg="blue").pack()
l2=Label(f2,text="Add work: ")
l2.place(x=10,y=190)
v=StringVar()

e1=Entry(f2,width=33,font=("times new roman",14),bd=2,textvariable=v)
e1.place(x=90,y=190)

def addd():
    lb1.insert(END,v.get())
    e1.delete(0,END)

b1=Button(f2,text="Add",width=10,bg="gray",fg="white",command=addd)
b1.place(x=400,y=190)

lb1=Listbox(f2,width=50,height=20,bd=2)
lb1.place(x=90,y=250)

def remove():
    lb1.delete(ANCHOR)

b2=Button(main,text="Remove",width=10,bg="gray",fg="white",command=remove)
b2.place(x=398,y=548)
main.mainloop()