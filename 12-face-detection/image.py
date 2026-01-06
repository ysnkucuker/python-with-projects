import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# Load Haar Cascade face detection model
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# ---------------- Functions ----------------

def select_image():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )

    if not file_path:
        return

    if not os.path.exists(file_path):
        messagebox.showerror("Error", "Image file not found.")
        return

    detect_faces(file_path)

def detect_faces(image_path):
    image = cv2.imread(image_path)

    if image is None:
        messagebox.showerror("Error", "Could not read the image.")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    show_image(image)

def show_image(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image_rgb)
    pil_image.thumbnail((500, 400))

    img_tk = ImageTk.PhotoImage(pil_image)
    image_label.config(image=img_tk)
    image_label.image = img_tk

# ---------------- GUI ----------------

window = tk.Tk()
window.title("Face Detection - Image")
window.geometry("550x500")

tk.Label(
    window,
    text="Face Detection from Image",
    font=("Arial", 14, "bold")
).pack(pady=10)

tk.Button(
    window,
    text="📁 Select Image",
    width=20,
    command=select_image
).pack(pady=10)

image_label = tk.Label(window)
image_label.pack(pady=10)

window.mainloop()
