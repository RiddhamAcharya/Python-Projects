import tkinter as tk
from tkinter import messagebox
import winsound

# ---------------- CONFIG ----------------
WIDTH = 280
HEIGHT = 280
RADIUS = 110

running = False
total_seconds = 1
remaining_seconds = 0


# ---------------- TIMER LOGIC ----------------
def start_timer(event=None):
    global running, total_seconds, remaining_seconds

    try:
        mins = float(entry.get())
        if mins <= 0:
            raise ValueError
    except:
        messagebox.showerror("Error", "Enter valid minutes")
        return

    total_seconds = int(mins * 60)
    remaining_seconds = total_seconds
    running = True
    update_timer()


def update_timer():
    global running, remaining_seconds

    if running and remaining_seconds >= 0:
        draw_clock()

        mins = remaining_seconds // 60
        secs = remaining_seconds % 60
        time_label.config(text=f"{mins:02}:{secs:02}")

        remaining_seconds -= 1
        root.after(1000, update_timer)

    elif remaining_seconds < 0:
        running = False
        alarm()


def pause_timer():
    global running
    running = False


def reset_timer():
    global running
    running = False
    canvas.delete("all")
    time_label.config(text="00:00")


def alarm():
    winsound.Beep(1200, 800)
    messagebox.showinfo("Time Up ⏰", "Your countdown is finished!")


# ---------------- ANALOG DRAW ----------------
def draw_clock():
    canvas.delete("all")

    cx, cy = WIDTH // 2, HEIGHT // 2

    # outer ring
    canvas.create_oval(cx-RADIUS, cy-RADIUS, cx+RADIUS, cy+RADIUS,
                       width=3, outline="#ff8c00")

    angle = (remaining_seconds / total_seconds) * 360
    extent = -angle

    canvas.create_arc(cx-RADIUS, cy-RADIUS, cx+RADIUS, cy+RADIUS,
                      start=90, extent=extent,
                      style="arc", width=10, outline="#ff8c00")


# ---------------- UI ----------------
root = tk.Tk()
root.title("Countdown Timer - Riddham")
root.geometry("360x520")
root.configure(bg="black")
root.resizable(False, False)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT,
                   bg="black", highlightthickness=0)
canvas.pack(pady=20)

time_label = tk.Label(root, text="00:00",
                      font=("Helvetica", 34),
                      fg="white", bg="black")
time_label.pack(pady=10)

entry = tk.Entry(root, justify="center", font=("Helvetica", 14))
entry.pack(pady=5)
entry.insert(0, "5")

tk.Label(root, text="Enter minutes",
         fg="white", bg="black").pack(pady=5)

btn_frame = tk.Frame(root, bg="black")
btn_frame.pack(pady=20)

start_btn = tk.Button(btn_frame, text="Start",
                      width=9, bg="#222", fg="white",
                      command=start_timer)
start_btn.grid(row=0, column=0, padx=8)

pause_btn = tk.Button(btn_frame, text="Pause",
                      width=9, bg="#222", fg="white",
                      command=pause_timer)
pause_btn.grid(row=0, column=1, padx=8)

reset_btn = tk.Button(btn_frame, text="Reset",
                      width=9, bg="#222", fg="white",
                      command=reset_timer)
reset_btn.grid(row=0, column=2, padx=8)

# ENTER key starts timer
root.bind("<Return>", start_timer)

root.mainloop()
