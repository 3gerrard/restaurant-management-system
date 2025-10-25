from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("restaurant msanagement system")
root.geometry("750x750")
root.configure(bg="lightblue")
Label(root,text="Odering System",font=("Arial",24),bg="lightblue", pady=10).pack(fill=X)
menu={"chicken sandwich":5,
      "big mac":4,
        "fries":2,
        "coke":1,
        "salad":3}
quantities={item:IntVar() for item in menu}
menu_frame=Frame(root,bg="lightblue",bd=5,
relief=RIDGE)
menu_frame.place(x=30,y=50,width=350,height=400)
Label(menu_frame,text="Menu",font=("Arial",14),bg="lightblue").pack()
Label(menu_frame,text="Item\t\tPrice (USd) \tQuantity",font=("Arial",12),bg="lightblue").pack(anchor=W)

for item, price in menu.items():
    f = Frame(menu_frame, bg="white")
    f.pack(fill=X, padx=10, pady=5)
    Label(f, text=item, font=("Arial", 12), width=10, anchor='w', bg="white").pack(side=LEFT)
    Label(f, text=f"{price}", font=("Arial", 12), width=10, bg="white").pack(side=LEFT)
    Entry(f, textvariable=quantities[item], font=("Arial", 12), width=5, justify='center', relief=SOLID).pack(side=LEFT, padx=5)

reciept_frame = Frame(root, bd=5, font=("Arial", 12), bg="white").pack()     
text_reciept = Text(reciept_frame, font=("courier", 12), bg="white")
text_reciept.pack(fill=BOTH, expand=1)

        