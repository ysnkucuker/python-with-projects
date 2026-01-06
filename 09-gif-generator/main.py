import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

images = []

def select_images():
    global images
    files = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Images", "*.png *.jpg *.jpeg")]
    )

    images = list(files)
    listbox.delete(0, tk.END)

    for img in images:
        listbox.insert(tk.END, img.split("/")[-1])

def create_gif():
    if not images:
        messagebox.showwarning("Warning", "Please select images first!")
        return

    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        duration = float(duration_entry.get())

        frames = []
        for path in images:
            img = Image.open(path).convert("RGB")
            img = img.resize((width, height))
            img = img.convert("P", palette=Image.ADAPTIVE)
            frames.append(img)

        frames[0].save(
            "result.gif",
            save_all=True,
            append_images=frames[1:],
            duration=int(duration * 1000),
            loop=0
        )

        messagebox.showinfo("Success", "GIF created: result.gif")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- GUI ----------------

window = tk.Tk()
window.title("🎞️ GIF Generator")
window.geometry("420x400")

tk.Button(window, text="📁 Select Images", command=select_images).pack(pady=5)

listbox = tk.Listbox(window, width=50)
listbox.pack(pady=5)

frame = tk.Frame(window)
frame.pack(pady=10)

tk.Label(frame, text="Width:").grid(row=0, column=0)
width_entry = tk.Entry(frame, width=6)
width_entry.insert(0, "300")
width_entry.grid(row=0, column=1)

tk.Label(frame, text="Height:").grid(row=0, column=2)
height_entry = tk.Entry(frame, width=6)
height_entry.insert(0, "300")
height_entry.grid(row=0, column=3)

tk.Label(frame, text="Duration (sec):").grid(row=1, column=0)
duration_entry = tk.Entry(frame, width=6)
duration_entry.insert(0, "0.5")
duration_entry.grid(row=1, column=1)

tk.Button(window, text="🎬 Create GIF", command=create_gif).pack(pady=10)

window.mainloop()
