# Python with Projects 🐍

This repository is designed to teach Python from scratch using hands-on projects.
Each **project** contains a standalone Python project that focuses on specific concepts,
from basics to more advanced topics.

## Repository Structure

Each project in this repository represents a **single Python project**.

## Projects

| Branch Name | Project | Concepts |
|------------|--------|---------|
| `01-cash-machine` | Cash Machine | print, variables, while loop, if-elif-else |
| `02-numeric_theories-n-algorithms` | Numeric Theories & Algorithms | factorial, fibonacci, armstrong number, perfect number, loops, functions |
| `03-numeric-algorithms-2` | Numeric Algorithms II | prime number, divisors, GCD, LCM, number pronunciation, pythagorean triples |
| `04-youtube-video-downloader` | YouTube Video Downloader | yt-dlp, file handling, subprocess, external tools integration |
| `05-remove-background` | Remove Background | rembg, image processing, file handling, AI-based background removal |
| `06-pdf-to-docx` | PDF to DOCX Converter | pdf2docx, file conversion, document processing |
| `07-qr-generator` | QR Code Generator | pyqrcode, svg generation, data encoding |
| `08-voice-recorder` | Voice Recorder | tkinter, sounddevice, soundfile, simpleaudio, multithreading, GUI, audio processing |
| `09-gif-generator` | GIF Generator | tkinter, Pillow, image processing, file handling, GUI automation |
| `10-counter-gui` | Countdown Timer GUI | tkinter, threading, time, GUI applications, state management |
| `11-desktop-notification` | Desktop Notification | tkinter, plyer, threading, time, desktop notifications |






## Descriptions

**04 – YouTube Video Downloader**  
A simple Python script that downloads YouTube videos as progressive MP4 files using `yt-dlp`.  
If VLC Media Player is installed, the downloaded video is automatically opened after completion.  
To run this project, the `yt-dlp` package must be installed (`pip install yt-dlp`).

**05 – Remove Background**  
A Python script that removes the background from images using the `rembg` library.  
GPU acceleration can be enabled for better performance by installing `rembg[gpu]`.
To run this project, the `rembg` package must be installed (`pip install "rembg[gpu]`).

**06 – PDF to DOCX Converter**  
A simple Python script that converts PDF documents into editable DOCX files using the `pdf2docx` library.  
Useful for document processing and automation workflows.
To run this project, the `pdf2docx` package must be installed (`pip install "pdf2docx`).

**08 - Voice Recorder**
A simple desktop voice recorder application built with Python and Tkinter.
It allows users to record audio from the microphone, monitor real-time input volume via a VU meter, save recordings as WAV files, and play them back through a graphical interface.
The project uses multithreading to ensure smooth recording without freezing the UI.
To run this project, the required packages must be installed (pip install sounddevice soundfile simpleaudio numpy).

**09 – GIF Generator**  
A desktop GUI application that creates animated GIFs from selected images using Python.  
Users can set image size and frame duration through a simple Tkinter interface.
To run this project, the required packages must be installed (PIL).

**11 – Desktop Notification**  
A simple desktop notification scheduler built with Python and Tkinter.  
Users can define a title, message, and delay time to receive system notifications.
To run this project, the required packages must be installed (plyer).






