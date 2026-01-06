import tkinter as tk
from plyer import notification
import time
import threading

def send_notification():
    title = title_entry.get()
    message = message_entry.get()

    try:
        delay = int(delay_entry.get())
    except:
        status_label.config(text="Delay must be a number!")
        return

    if not title or not message:
        status_label.config(text="Enter title and message!")
        return

    status_label.config(text="⏳ Waiting to send notification...")
    threading.Thread(
        target=wait_and_notify,
        args=(title, message, delay),
        daemon=True
    ).start()

def wait_and_notify(title, message, delay):
    time.sleep(delay)
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )
    status_label.config(text="✅ Notification sent")

# ---------------- GUI ----------------

window = tk.Tk()
window.title("🔔 Desktop Notification")
window.geometry("320x260")

tk.Label(window, text="Title").pack()
title_entry = tk.Entry(window, width=35)
title_entry.pack(pady=5)

tk.Label(window, text="Message").pack()
message_entry = tk.Entry(window, width=35)
message_entry.pack(pady=5)

tk.Label(window, text="Delay (sec)").pack()
delay_entry = tk.Entry(window, width=10)
delay_entry.insert(0, "5")
delay_entry.pack(pady=5)

tk.Button(
    window,
    text="🔔 Send Notification",
    command=send_notification
).pack(pady=10)

status_label = tk.Label(window, text="Ready")
status_label.pack()

window.mainloop()
