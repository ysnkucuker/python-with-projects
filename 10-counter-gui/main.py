import tkinter as tk
import time
import threading

running = False

def start():
    global running
    if running:
        return

    try:
        hours = int(hours_entry.get())
        minutes = int(minutes_entry.get())
        seconds = int(seconds_entry.get())
        total_seconds = hours * 3600 + minutes * 60 + seconds
    except:
        status_label.config(text="Invalid input!")
        return

    if total_seconds <= 0:
        status_label.config(text="Time cannot be zero!")
        return

    running = True
    threading.Thread(
        target=countdown,
        args=(total_seconds,),
        daemon=True
    ).start()

def countdown(duration):
    global running
    while duration >= 0 and running:
        hours = duration // 3600
        minutes = (duration % 3600) // 60
        seconds = duration % 60

        time_label.config(
            text=f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        )
        time.sleep(1)
        duration -= 1

    if duration < 0 and running:
        status_label.config(text="⏰ Time is up!")
        running = False

def stop():
    global running
    running = False
    status_label.config(text="⏸️ Stopped")

# ---------------- GUI ----------------

window = tk.Tk()
window.title("⏳ Countdown Timer")
window.geometry("300x220")

time_label = tk.Label(
    window,
    text="00:00:00",
    font=("Arial", 28)
)
time_label.pack(pady=10)

frame = tk.Frame(window)
frame.pack()

hours_entry = tk.Entry(frame, width=4)
hours_entry.insert(0, "0")
hours_entry.grid(row=0, column=0)

tk.Label(frame, text=":").grid(row=0, column=1)

minutes_entry = tk.Entry(frame, width=4)
minutes_entry.insert(0, "0")
minutes_entry.grid(row=0, column=2)

tk.Label(frame, text=":").grid(row=0, column=3)

seconds_entry = tk.Entry(frame, width=4)
seconds_entry.insert(0, "0")
seconds_entry.grid(row=0, column=4)

tk.Button(
    window,
    text="▶ Start",
    width=12,
    command=start
).pack(pady=5)

tk.Button(
    window,
    text="⏸ Stop",
    width=12,
    command=stop
).pack(pady=5)

status_label = tk.Label(window, text="Ready")
status_label.pack(pady=5)

window.mainloop()
