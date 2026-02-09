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
| `12-face-detection` | Face Detection | opencv, haar cascade, computer vision, tkinter, image processing |
| `13-image-resizer` | Image Resizer | tkinter, pillow, image processing, batch processing, file handling |
| `14-speech-to-text` | Speech to Text | speechrecognition, tkinter, threading, microphone, AI-based speech recognition |
| `15-oop` | Object Oriented Programming | classes, objects, constructors, methods, inheritance, super(), method overriding, magic methods |
| `16-remote-control` | TV Remote Control | OOP, classes, objects, methods, magic methods, state management, user input |
| `17-turtle-tutorial` | Turtle Graphics Tutorial | turtle, graphics programming, functions, modules, loops, user interaction |
| `18-catch-the-turtle` | Catch the Turtle Game | turtle, event handling, onclick, random positioning, timer, score system |
| `19-snake` | Snake Game | turtle, game loop, keyboard controls, collision detection, walls, pause system, score tracking |
| `20-tetris` | Tetris Game | turtle, falling blocks, rotation, line clearing, score tracking |
| `21-grade-calculator` | Grade Calculator | file handling, functions, conditional logic, string parsing, data processing |
| `22-bmi-calculator` | BMI Calculator | tkinter, GUI, input validation, functions, conditional logic, error handling |
| `23-secret-file` | Encrypted Notes App | tkinter, cryptography, file handling, encryption/decryption, dark mode |
| `24-library-system-sqlite` | Library Management System | python, sqlite, OOP, CRUD operations, CLI, database management |
| `25-house-prices-data-analysis` | House Prices Data Analysis | python, pandas, numpy, matplotlib, data cleaning, exploratory data analysis |
| `26-github-profile-analyzer` | GitHub Profile Analyzer | python, requests, beautifulsoup4, web scraping, data extraction, profile analysis |
| `27-smtp-email` | SMTP Email Sender | python, smtplib, email, smtp, gmail, app password, email automation |
| `28-user-login-register` | User Login & Registration | python, PyQt5, sqlite3, GUI, user authentication, register, login |
| `29-notepad` | Advanced Notepad | python, PyQt5, GUI, text editor, line numbers, find and replace, file handling |
| `30-crypto-crazy` | Crypto Trading Bot | python, requests, crypto, binance api, trading bot, moving average, paper trading |



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

**12 – Face Detection (Webcam & Image)**  
A computer vision project that detects human faces using OpenCV and Haar Cascade classifiers.  
The project includes two different usage modes:
- **Webcam detection:** Performs real-time face detection using the system camera.
- **Image detection:** Allows users to select an image from their computer via a Tkinter GUI and detects faces on the selected image.

This project demonstrates the difference between real-time video processing and static image analysis in computer vision workflows.

**13 – Image Resizer**  
A desktop application that allows users to select multiple images and resize them in batch.  
Built with Tkinter and Pillow, this project demonstrates image processing, file handling, and GUI-based user interaction.
To run this project, the required packages must be installed (pillow).

**14 – Speech to Text**  
A desktop application that converts spoken language into text using a microphone.  
Built with Tkinter and the SpeechRecognition library, this project demonstrates real-time audio capture, threading, and AI-based speech recognition using Google's speech API.
To run this project, the required packages must be installed (pip install SpeechRecognition pyaudio).

**16 – TV Remote Control**  
A console-based Python application that simulates a television remote control using Object-Oriented Programming principles.  
The project demonstrates class design, state management, user interaction, magic methods (`__str__`, `__len__`), and dynamic channel handling.

**19 – Snake Game**
A silent Snake game built with Python’s turtle module.
The game includes visible walls, a restricted play area, pause/resume support (P key), a time counter, and permanent top 3 high score tracking.
Touching a wall or the snake’s body ends the game.
No external libraries are required.

**24 – Library Management System (SQLite)**
A console-based Python application that manages books using SQLite with basic CRUD operations and Object-Oriented Programming.
SQLite is a lightweight, file-based database and can be downloaded from the official website if needed: https://www.sqlite.org/download.html

**30 – Crypto Crazy**
A Python-based crypto trading simulation using the requests library and a public exchange API (Binance).
The application fetches real-time cryptocurrency prices, analyzes market data using a simple moving average strategy, and generates BUY / SELL / HOLD signals.
It is designed for educational and paper trading purposes only and does not execute real trades.
No API key is required, and no external libraries are used beyond requests.








