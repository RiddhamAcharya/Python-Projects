import tkinter as tk

# ----------------- Timer Logic -----------------
running = False
seconds = 0

def update_timer():
    global seconds
    if running:
        seconds += 1
        mins = seconds // 60
        secs = seconds % 60
        time_label.config(text=f"{mins:02}:{secs:02}")
        root.after(1000, update_timer)

def start_timer():
    global running
    if not running:
        running = True
        update_timer()

def pause_timer():
    global running
    running = False

def reset_timer():
    global running, seconds
    running = False
    seconds = 0
    time_label.config(text="00:00")

# ----------------- UI -----------------
root = tk.Tk()
root.title("Timer App - Riddham")
root.geometry("300x200")
root.resizable(False, False)

time_label = tk.Label(root, text="00:00", font=("Helvetica", 40))
time_label.pack(pady=20)

btn_frame = tk.Frame(root)
btn_frame.pack()

start_btn = tk.Button(btn_frame, text="Start", width=8, command=start_timer)
pause_btn = tk.Button(btn_frame, text="Pause", width=8, command=pause_timer)
reset_btn = tk.Button(btn_frame, text="Reset", width=8, command=reset_timer)

start_btn.grid(row=0, column=0, padx=5)
pause_btn.grid(row=0, column=1, padx=5)
reset_btn.grid(row=0, column=2, padx=5)

root.mainloop()
