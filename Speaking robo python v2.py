from win32com.client import Dispatch
import re
import tkinter as tk
from tkinter import ttk

def speak_text(text):
    try:
        speaker = Dispatch("SAPI.SpVoice")
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
        for sentence in sentences:
            speaker.Speak(sentence)
    except Exception as e:
        print(f"Error: {e}")

def on_speak_button_click():
    user_input = text_entry.get("1.0", tk.END).strip()
    if user_input:
        speak_text(user_input)

# Create the main window
root = tk.Tk()
root.title("Jarvis Text-to-Speech")
root.geometry("400x300")
root.configure(bg="#1e1e1e")  # Dark background color

# Create and configure the text entry
text_entry = tk.Text(root, wrap="word", width=40, height=10, bg="#1e1e1e", fg="white", insertbackground="white")
text_entry.pack(pady=10)
text_entry.insert("1.0", "Enter the text you want to be spoken here...")

# Create and configure the speak button
speak_button = ttk.Button(root, text="Speak", command=on_speak_button_click)
speak_button.pack(pady=10)

# Run the GUI
root.mainloop()
