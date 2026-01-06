import tkinter as tk
from tkinter import ttk
import sounddevice as sd
import soundfile as sf
import numpy as np
import simpleaudio as sa
import threading

# Audio settings
fs = 44100
recording = []
is_recording = False
file_name = "recording.wav"

# ---------------- Functions ----------------

def start_recording():
    global is_recording, recording
    recording = []
    is_recording = True
    status_label.config(text="🔴 Recording")
    threading.Thread(target=record_audio, daemon=True).start()

def record_audio():
    global recording
    # Open microphone input stream
    with sd.InputStream(samplerate=fs, channels=1, callback=audio_callback):
        while is_recording:
            sd.sleep(100)

def audio_callback(indata, frames, time, status):
    global recording
    recording.append(indata.copy())

    # Audio level (VU Meter)
    level = int(np.linalg.norm(indata) * 200)
    level = min(level, 100)
    level_bar["value"] = level

def stop_recording():
    global is_recording
    is_recording = False
    status_label.config(text="⏹️ Recording Stopped")

def save_recording():
    if recording:
        audio = np.concatenate(recording)
        sf.write(file_name, audio, fs)
        status_label.config(text="💾 Recording Saved")

def play_recording():
    try:
        wave = sa.WaveObject.from_wave_file(file_name)
        wave.play()
    except:
        status_label.config(text="⚠️ Please record first!")

# ---------------- GUI ----------------

window = tk.Tk()
window.title("🎤 Voice Recorder")
window.geometry("300x300")

status_label = tk.Label(window, text="Ready", font=("Arial", 12))
status_label.pack(pady=10)

level_bar = ttk.Progressbar(window, length=200, maximum=100)
level_bar.pack(pady=10)

tk.Button(window, text="▶ Start Recording", width=20, command=start_recording).pack(pady=5)
tk.Button(window, text="⏹ Stop", width=20, command=stop_recording).pack(pady=5)
tk.Button(window, text="💾 Save", width=20, command=save_recording).pack(pady=5)
tk.Button(window, text="🔊 Play", width=20, command=play_recording).pack(pady=5)

window.mainloop()
