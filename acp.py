from tkinter import *
from tkinter import messagebox

# Create the window
root = Tk()
root.title("Restaurant Management System")
root.geometry("750x750")
root.configure(bg="lightblue")

# Title Label
Label(root, text="ORDERING MANAGEMENT SYSTEM", font=("Arial", 18, "bold"), bg="#4a90e2", fg="white", pady=10).pack(fill=X)

# Menu items and their prices
menu = {
    "Burger": 250,
    "Pizza": 600,
    "Fries": 150,
    "Coke": 80,
    "Coffee": 120,
    "Juice": 100
}

# Store quantities
quantities = {item: IntVar() for item in menu}

# ===== MENU FRAME =====
menu_frame = Frame(root, bd=5, relief=RIDGE, bg="white")
menu_frame.place(x=30, y=100, width=350, height=400)
Label(menu_frame, text="Menu", font=("Arial", 14, "bold"), bg="white", fg="black").pack()
Label(menu_frame, text="Item\t\tPrice (KSh)\tQty", font=("Arial", 12, "bold"), bg="white", fg="black").pack()

# Display menu items
for item, price in menu.items():
    f = Frame(menu_frame, bg="white")
    f.pack(fill=X, padx=10, pady=5)
    Label(f, text=item, font=("Arial", 12), width=10, anchor='w', bg="white").pack(side=LEFT)
    Label(f, text=f"{price}", font=("Arial", 12), width=10, bg="white").pack(side=LEFT)
    Entry(f, textvariable=quantities[item], font=("Arial", 12), width=5, justify='center', relief=SOLID).pack(side=LEFT, padx=5)

# ===== RECEIPT FRAME =====
receipt_frame = Frame(root, bd=5, relief=RIDGE, bg="white")
receipt_frame.place(x=410, y=100, width=310, height=400)

Label(receipt_frame, text="Receipt", font=("Arial", 14, "bold"), bg="white").pack()
text_receipt = Text(receipt_frame, font=("Courier", 10), bg="#f8f8f8")
text_receipt.pack(fill=BOTH, expand=True)

# ===== TOTAL FRAME =====
total_frame = Frame(root, bd=5, relief=RIDGE, bg="white")
total_frame.place(x=30, y=520, width=690, height=120)

total_var = StringVar()
Label(total_frame, text="Total (KSh):", font=("Arial", 14, "bold"), bg="white").place(x=20, y=20)
Entry(total_frame, textvariable=total_var, font=("Arial", 14), width=15, state='readonly', justify='center').place(x=160, y=20)

# ===== FUNCTIONS =====
def calculate_total():
    total = 0
    for item, price in menu.items():
        qty = quantities[item].get()
        total += price * qty
    total_var.set(f"{total:.2f}")
    return total

def generate_receipt():
    total = calculate_total()
    text_receipt.delete(1.0, END)
    text_receipt.insert(END, "        RECEIPT\n")
    text_receipt.insert(END, "-" * 30 + "\n")

    for item, price in menu.items():
        qty = quantities[item].get()
        if qty > 0:
            text_receipt.insert(END, f"{item:15} x{qty:<3} = KSh {price * qty}\n")

    text_receipt.insert(END, "-" * 30 + "\n")
    text_receipt.insert(END, f"TOTAL: KSh {total:.2f}\n")
    text_receipt.insert(END, "Thank you for your order!\n")

def clear_all():
    for item in menu:
        quantities[item].set(0)
    total_var.set("")
    text_receipt.delete(1.0, END)

def exit_app():
    confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if confirm:
        root.destroy()

# ===== BUTTONS =====
Button(total_frame, text="Calculate Total", font=("Arial", 12, "bold"), bg="#4a90e2", fg="white", width=15, command=calculate_total).place(x=360, y=20)
Button(total_frame, text="Generate Receipt", font=("Arial", 12, "bold"), bg="#28a745", fg="white", width=15, command=generate_receipt).place(x=520, y=20)
Button(total_frame, text="Clear", font=("Arial", 12, "bold"), bg="#dc3545", fg="white", width=10, command=clear_all).place(x=160, y=70)
Button(total_frame, text="Exit", font=("Arial", 12, "bold"), bg="#6c757d", fg="white", width=10, command=exit_app).place(x=280, y=70)

root.mainloop()