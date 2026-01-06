import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

images = []

# ---------------- Functions ----------------

def select_images():
    global images
    files = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )

    images = list(files)
    listbox.delete(0, tk.END)

    for img in images:
        listbox.insert(tk.END, img.split("/")[-1])

def resize_images():
    if not images:
        messagebox.showwarning("Warning", "Please select images first!")
        return

    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
    except:
        messagebox.showerror("Error", "Width and height must be numbers!")
        return

    for path in images:
        img = Image.open(path)
        img = img.resize((width, height))

        file_name, ext = path.rsplit(".", 1)
        save_path = f"{file_name}_resized.{ext}"
        img.save(save_path)

    messagebox.showinfo(
        "Success",
        f"{len(images)} images have been resized successfully!"
    )

# ---------------- GUI ----------------

window = tk.Tk()
window.title("🖼️ Image Resizer")
window.geometry("400x400")

tk.Button(
    window,
    text="📁 Select Images",
    command=select_images
).pack(pady=5)

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

tk.Button(
    window,
    text="🔄 Resize Images",
    command=resize_images
).pack(pady=10)

window.mainloop()
