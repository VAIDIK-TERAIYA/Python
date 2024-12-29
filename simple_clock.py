import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("Simple Clock")

# Set the size of the window
root.geometry("250x100")

# Function to update the time
def update_time():
    current_time = time.strftime("%H:%M:%S")  # Format the time as HH:MM:SS
    label.config(text=current_time)  # Update the label with the current time
    label.after(1000, update_time)  # Call the update_time function every 1000 ms (1 second)

# Create a label to display the time
label = tk.Label(root, font=("calibri", 40, "bold"), background="black", foreground="white")
label.pack(anchor='center')

# Start the time update
update_time()

# Run the Tkinter event loop
root.mainloop()
