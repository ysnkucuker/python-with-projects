import tkinter as tk
import speech_recognition as sr
import threading

# ---------------- Functions ----------------

def start_recording():
    # Run speech recognition in a separate thread
    threading.Thread(target=speech_to_text, daemon=True).start()

def speech_to_text():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            status_label.config(text="🎙️ Listening...")
            audio = recognizer.listen(source)

        # Convert speech to text using Google Speech Recognition
        text = recognizer.recognize_google(audio, language="tr-TR")

        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, text)
        status_label.config(text="✅ Completed")

    except sr.UnknownValueError:
        status_label.config(text="⚠️ Could not understand audio")

    except sr.RequestError:
        status_label.config(text="⚠️ Speech service unavailable")

# ---------------- GUI ----------------

window = tk.Tk()
window.title("🎤 Speech to Text")
window.geometry("400x300")

text_box = tk.Text(window, height=10, width=45)
text_box.pack(pady=10)

tk.Button(
    window,
    text="▶ Start Recording",
    command=start_recording
).pack(pady=5)

status_label = tk.Label(window, text="Ready")
status_label.pack(pady=5)

window.mainloop()
