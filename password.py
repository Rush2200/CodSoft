from tkinter import * 
import string 
import random 
  
def generator(): 
     small_alphabets=string.ascii_lowercase 
     capital_alphabets=string.ascii_uppercase 
     numbers=string.digits 
     special_charecters=string.punctuation 
     all=small_alphabets+capital_alphabets+numbers+special_charecters 
     
  
     if choice.get()==1: 
         passwordField.insert(0,random.sample(small_alphabets,5)) 
  
     if choice.get()==2: 
         passwordField.insert(0,random.sample(small_alphabets+numbers+capital_alphabets,8)) 
  
     if choice.get()==3: 
         passwordField.insert(0,random.sample(all,10)) 
  
  
root=Tk() 
root.config(bg='black') 
root.title("Password_Generator")
root.minsize(height=350,width=250)
root.maxsize(height=350,width=250)
choice=IntVar() 
Font=('arial',13,'bold') 
passwordLabel=Label(root,text='Password Generator',font=('times new roman',20,'bold'),bg='black',fg='white') 
passwordLabel.grid(pady=10) 
weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font) 
weakradioButton.grid(pady=5) 
  
mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font) 
mediumradioButton.grid(pady=5) 
  
strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font) 
strongradioButton.grid(pady=5) 

l1=Label(root,text="",height=2,bg="black")
l1.grid(pady=5)
  
generateButton=Button(root,text='Generate',font=Font,bg="green",command=generator) 
generateButton.grid(pady=5) 
  
passwordField=Entry(root,width=25,bd=2,font=Font) 
passwordField.grid() 
  
root.mainloop()