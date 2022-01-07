import tkinter as tk
w=tk.Tk()

hours=tk.Entry(w)
hours.grid(row=1,column=2)
minimumwage=tk.Label(text="15.00 * ").grid(row=1,column=1)
incometax=tk.Label(text=" * 0.78").grid(row=1,column=3)
direction=tk.Label(text="Please Print # Of hours worked below then press enter").grid(row=0,column=2)

def calculate(event):
    a=int(hours.get())
    b=15.00
    c=0.78
    d= a*b*c
    e=str(d)
    incomeaftertax=tk.Label(text="The Income after Income tax is: "+ e).grid(row=2,column=2)
    w.after(6000,incomeaftertax.destroy)


hours.bind("<Return>",calculate)

w.mainloop()