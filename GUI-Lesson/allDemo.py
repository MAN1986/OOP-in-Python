
# from tkinter import *
# # import tkinter as tk
# top=Tk()
# # from tkinter import Label # get a widget
# widget = Label(top, text='Hello World') # make a Label
# widget.pack() # arrange it in its parent

# # Label(top, text='Hello World').pack()

# mainloop() # start the event loop



# ### Layout Demos ###
# ### Geometry Manager ###

# ''' There can be three ways for this '''

# ### 1- Pack layout ###
# import tkinter as tk
# root = tk.Tk()
# w = tk.Label(root, text="Red Sun", bg="red", fg="white")
# w.pack()
# # Or use one statement as:
# #tk.Label(root, text="Red Sun", bg="red", fg="white").pack()
# w = tk.Label(root, text="Green Grass", bg="green", fg="black")
# w.pack()
# w = tk.Label(root, text="Blue Sky", bg="blue", fg="white")
# w.pack()
# tk.mainloop()


# ### Pack with Fill ###
# import tkinter as tk
# root = tk.Tk()
# w = tk.Label(root, text="Red Sun", bg="red", fg="white")
# w.pack(fill=tk.X)
# w = tk.Label(root, text="Green Grass", bg="green", fg="black")
# w.pack(fill=tk.X)
# w = tk.Label(root, text="Blue Sky", bg="blue", fg="white")
# w.pack(fill=tk.X)
# tk.mainloop()


# ## Pack with Padding ##
# import tkinter as tk

# root = tk.Tk()
# w = tk.Label(root, text="Red Sun", bg="red", fg="white")
# w.pack(fill=tk.X, padx=10, pady=5)
# w = tk.Label(root, text="Green Grass", bg="green", fg="black")
# w.pack(fill=tk.X, padx=10, pady=5)
# w = tk.Label(root, text="Blue Sky", bg="blue", fg="white")
# w.pack(fill=tk.X, padx=10, pady=5)
# tk.mainloop()

# ## Pack Horizontally ##
# from tkinter import *
# root = Tk()
# w = Label(root, text="Red", bg="red", fg="white")
# w.pack(side=LEFT, padx=10, pady=10) #Default side=TOP
# w = Label(root, text="Green", bg="green", fg="black")
# w.pack(side=LEFT, padx=10, pady=10)
# w = Label(root, text="Blue", bg="blue", fg="white")
# w.pack(side=LEFT, padx=10, pady=10)
# mainloop()

# ### 2- Grid layout ###

# ## Simple row and column method ##
# from tkinter import *
# root = Tk()
# w = Label(root, text="Red", bg="red", fg="white")
# w.grid(row=0,column=0,padx=10, pady=10)
# w = Label(root, text="Green", bg="green", fg="black")
# w.grid(row=1,column=0,padx=10, pady=10)
# w = Label(root, text="Blue", bg="blue", fg="white")
# w.grid(row=2,column=0,padx=10, pady=10)
# mainloop()


# ## Simple row and column method with padding##
# from tkinter import *
# root = Tk()
# w = Label(root, text="Red", bg="red", fg="white",padx=20, pady=2)
# # The padx and pady in above statement sets the size of the label
# w.grid(row=0,column=0,columnspan=2,padx=10, pady=10)
# w = Label(root, text="Green", bg="green", fg="black")
# w.grid(row=1,column=0,padx=10, pady=10)
# w = Label(root, text="Blue", bg="blue", fg="white")
# w.grid(row=1,column=1,padx=10, pady=10)
# mainloop()
# '''Note that the widgets are centered in their cells.
# You can use the sticky option to change this
# this option takes one or more values from the set N, S, E, W.
# To align the labels to the left border, you could use W (west)'''


# ### 3- Place layout ###
# from tkinter import *
# root = Tk()
# # width x height + x_offset + y_offset:
# root.geometry("170x200+30+30")

# w = Label(root, text="Red", bg="red", fg="white")
# w.place(x = 0, y = 30, width=120, height=25)
# w = Label(root, text="Green", bg="green", fg="black")
# w.place(x = 20, y = 60, width=120, height=25)
# w = Label(root, text="Blue", bg="blue", fg="white")
# w.place(x = 20, y = 90, width=120, height=25)
# mainloop()

# ''' The Variable Classes '''
# '''The Variable Classes (BooleanVar, DoubleVar, IntVar, StringVar)
# We can use get() to get variable value
# set() to set new value
# and trace() to trace a value if it gets updated
# '''



# ''' Call Back Functions '''

# from tkinter import *
# def myFunc():
#     global x
#     x+=1
#     t.set(f"I clicked the button {x}th time")
    
# x=0
# root=Tk()
# t=StringVar()
# myButton=Button(root,text='Press',padx=10,pady=10,command=myFunc)
# myButton.pack()
# myLabel=Label(root,textvariable=t)
# myLabel.pack()
# root.mainloop()


''' Calculator Example '''
from tkinter import *
def button_click(n):
    global v
    p=str(v.get())
    m=p+str(n)
    v.set(str(m))
def button_clear():
    global v
    v.set('')
def button_add():
    global first,v
    first=int(v.get())
    v.set('')
def button_result():
    second=int(v.get())
    result=first+second
    v.set(str(result))
root=Tk()
root.title("My Calculator")
v=StringVar()
e=Label(root,width=50,borderwidth=5,textvariable=v,relief=GROOVE)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

b1=Button(root,text='1',padx=40,pady=20,command=lambda : button_click(1))
b1.grid(row=1,column=0)
b2=Button(root,text='2',padx=40,pady=20,command=lambda : button_click(2))
b2.grid(row=1,column=1)
b3=Button(root,text='3',padx=40,pady=20,command=lambda : button_click(3))
b3.grid(row=1,column=2)

b4=Button(root,text='4',padx=40,pady=20,command=lambda : button_click(4))
b4.grid(row=2,column=0)
b5=Button(root,text='5',padx=40,pady=20,command=lambda : button_click(5))
b5.grid(row=2,column=1)
b6=Button(root,text='6',padx=40,pady=20,command=lambda : button_click(6))
b6.grid(row=2,column=2)

b7=Button(root,text='7',padx=40,pady=20,command=lambda : button_click(7))
b7.grid(row=3,column=0)
b8=Button(root,text='8',padx=40,pady=20,command=lambda : button_click(8))
b8.grid(row=3,column=1)
b9=Button(root,text='9',padx=40,pady=20,command=lambda : button_click(9))
b9.grid(row=3,column=2)

b0=Button(root,text='0',padx=40,pady=20,command=lambda : button_click(0))
b0.grid(row=4,column=0)

b10=Button(root,text='+',padx=69,pady=20,command=lambda : button_add())
b10.grid(row=4,column=1,columnspan=2)
b11=Button(root,text='=',padx=39,pady=20,command=lambda : button_result())
b11.grid(row=5,column=0)
b12=Button(root,text='Clear',padx=60,pady=20,command=lambda : button_clear())
b12.grid(row=5,column=1,columnspan=2)

root.mainloop()
