import tkinter as tk
from tkinter import ttk, messagebox
from cryptography.fernet import Fernet, InvalidToken
import base64
import hashlib
import os

FILE_NAME = "secretfile.txt"

# --------- KEY DERIVATION ----------
def generate_key(master_key: str) -> bytes:
    hash_key = hashlib.sha256(master_key.encode()).digest()
    return base64.urlsafe_b64encode(hash_key)

# --------- MAIN APP ----------
class CryptoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secret File")
        self.root.geometry("420x620")
        self.root.resizable(False, False)

        self.dark_mode = False
        self.build_ui()
        self.apply_theme()

    def build_ui(self):
        self.main = ttk.Frame(self.root)
        self.main.pack(fill="both", expand=True, padx=10, pady=10)

        ttk.Label(self.main, text="Title").pack(anchor="w")
        self.title_entry = ttk.Entry(self.main)
        self.title_entry.pack(fill="x", pady=5)

        ttk.Label(self.main, text="Context").pack(anchor="w")
        self.text_box = tk.Text(self.main, height=15, wrap="word")
        self.text_box.pack(fill="both", expand=True, pady=5)

        ttk.Label(self.main, text="Enter Master Key").pack(anchor="w")
        self.key_entry = ttk.Entry(self.main, show="*")
        self.key_entry.pack(fill="x", pady=5)

        btn_frame = ttk.Frame(self.main)
        btn_frame.pack(fill="x", pady=10)

        ttk.Button(btn_frame, text="Save & Encrypt", command=self.encrypt_save).pack(side="left", expand=True, fill="x", padx=3)
        ttk.Button(btn_frame, text="Decrypt", command=self.decrypt_load).pack(side="left", expand=True, fill="x", padx=3)

        self.dark_btn = ttk.Button(self.main, text="🌙 Dark Mode", command=self.toggle_dark)
        self.dark_btn.pack(fill="x")

    # --------- ENCRYPT ----------
    def encrypt_save(self):
        title = self.title_entry.get()
        text = self.text_box.get("1.0", "end-1c")
        master_key = self.key_entry.get()

        if not title or not text or not master_key:
            messagebox.showwarning("Warning", "All fields required!")
            return

        key = generate_key(master_key)
        fernet = Fernet(key)

        encrypted_text = fernet.encrypt(text.encode()).decode()

        # 🔹 APPEND MODE
        with open(FILE_NAME, "a", encoding="utf-8") as f:
            f.write("\n---ENTRY---\n")
            f.write(title + "\n")
            f.write(encrypted_text + "\n")

        # 🔹 CLEAN INPUTS
        self.title_entry.delete(0, "end")
        self.text_box.delete("1.0", "end")
        self.key_entry.delete(0, "end")

        messagebox.showinfo("Success", "Encrypted & appended successfully!")

    # --------- DECRYPT ----------
    def decrypt_load(self):
        master_key = self.key_entry.get()

        if not master_key:
            messagebox.showwarning("Warning", "Enter master key!")
            return

        if not os.path.exists(FILE_NAME):
            messagebox.showerror("Error", "secretfile.txt not found!")
            return

        with open(FILE_NAME, "r", encoding="utf-8") as f:
            content = f.read().strip()

        # 🔹 FIRST RECORD
        if not content.startswith("---ENTRY---"):
            content = "---ENTRY---\n" + content

        entries = [e.strip() for e in content.split("---ENTRY---") if e.strip()]

        key = generate_key(master_key)
        fernet = Fernet(key)

        # 🔹 TRY ALL ENTRIES
        for entry in entries:
            lines = entry.splitlines()

            if len(lines) < 2:
                continue  # PASS

            title = lines[0].strip()
            encrypted_text = lines[1].strip()

            try:
                decrypted = fernet.decrypt(encrypted_text.encode()).decode()

                # SUCCESS
                self.title_entry.delete(0, "end")
                self.title_entry.insert(0, title)

                self.text_box.delete("1.0", "end")
                self.text_box.insert("1.0", decrypted)

                messagebox.showinfo("Success", "Decrypted successfully!")
                return

            except InvalidToken:
                continue

        #  UNSUCCESS
        messagebox.showerror("Error", "Wrong master key!")

    # --------- DARK MODE ----------
    def toggle_dark(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()

    def apply_theme(self):
        bg = "#1e1e1e" if self.dark_mode else "#f0f0f0"
        fg = "#ffffff" if self.dark_mode else "#000000"

        self.root.configure(bg=bg)
        self.main.configure(style="Main.TFrame")

        style = ttk.Style()
        style.configure("Main.TFrame", background=bg)
        style.configure("TLabel", background=bg, foreground=fg)
        style.configure("TButton", background=bg)

        self.text_box.configure(
            bg="#2b2b2b" if self.dark_mode else "white",
            fg="white" if self.dark_mode else "black",
            insertbackground="white" if self.dark_mode else "black"
        )

# --------- RUN ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoApp(root)
    root.mainloop()
