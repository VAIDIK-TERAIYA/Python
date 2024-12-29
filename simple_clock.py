import tkinter as tk
import time

root = tk.Tk()
root.title("Simple Clock")

root.geometry("250x100")

def update_time():
    current_time = time.strftime("%H:%M:%S")  
    label.config(text=current_time) 
    label.after(1000, update_time) 

label = tk.Label(root, font=("calibri", 40, "bold"), background="black", foreground="white")
label.pack(anchor='center')

update_time()

root.mainloop()
