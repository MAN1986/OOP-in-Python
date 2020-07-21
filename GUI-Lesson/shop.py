import tkinter as tk 
from tkinter import ttk 
products={'anjeer':2500,'pista':2700,'badaam':2000,'chalghoza':8000}
option='y'
bill=0
F=[]
Q=[]
# while(option=='y' or option=='Y'):
#     p=input('Enter product to buy: ')
#     price=products.get(p)
#     q=eval(input('Enter quantity: '))
#     F.append(p)
#     Q.append(q)
#     bill+=price*q
#     option=input("You want to buy more: (y/n): ")
# #Bill Generation
# for i in range(len(F)):
#     print(F[i]+"\t"+str(Q[i])+"\t"+str(Q[i]*products[F[i]]))
# print("Total Bill= "+str(bill))



# Creating tkinter window 
window = tk.Tk() 
window.title('Dry Fruit Shop') 
# width x height + x_offset + y_offset:
window.geometry('800x650+30+30')
Q=[]
P=[]
line=0
def clicked():
    global line
    l1=tk.Label(window, text = "Select the Item :", font = ("Times New Roman", 10))
    l1.place(x = 120, y = 10+(line*30), width=100, height=25)

    n = tk.StringVar()
    n.trace("w", callback1)
    prodCombo = ttk.Combobox(window, width = 27, textvariable = n) 
    prodCombo['values'] = list(products.keys())  
    prodCombo.place(x = 220, y = 10+(line*30), width=80, height=25) 
    prodCombo.current(0) 

    l2=tk.Label(window, text = "Quantity (Kg) :", font = ("Times New Roman", 10))
    l2.place(x = 320, y = 10+(line*30), width=100, height=25) 

    m = tk.DoubleVar()
    m.trace("w", callback1)
    qCombo = ttk.Combobox(window, width = 7, textvariable = m)  
    qCombo['values'] = [.25,.5,.75,1,1.5,2,2.5,3] 
    qCombo.place(x = 420, y = 10+(line*30), width=80, height=25) 

    newEntryButton=tk.Button(window,text='Purchase Item',padx=20,pady=20,command=clicked)  
    newEntryButton.place(x = 10, y = 10+(line*30+30), width=100, height=25)

    P.append(n)
    Q.append(m)
    billEntry['text']=str(billCalculation())
    line+=1
    
def billCalculation():
    price=0
    for i in range(len(P)):
        if (products.get(P[i].get()) is not None):
            price+=(Q[i].get())*products.get(P[i].get())
    billEntry['text']=str(price)
    # return price
def callback1(*args):
    billCalculation()

newEntryButton=tk.Button(window,text='Purchase Item',padx=20,pady=20,command=clicked)  
newEntryButton.place(x = 10, y = 10, width=100, height=25)
# label 


l3=tk.Label(window, text = "Total Price :", font = ("Times New Roman", 10)) 
l3.place(x = 500, y = 80, width=120, height=25)


billEntry=tk.Label(window,borderwidth=2, relief="groove")
billEntry['text']=str(billCalculation())
billEntry.place(x = 600, y = 80, width=120, height=25)

window.mainloop()
