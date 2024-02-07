from gtts import gTTS
import os
import tkinter as tk
from tkinter import ttk, filedialog
from datetime import datetime
import pygame

class TextToSpeechApp:
    def __init__(self, master):
        self.master = master
        master.title("Text to Speech Converter System")

        style = ttk.Style()
        style.configure("TButton", padding=10, font=('Arial', 12), background='#3498db', foreground='white')
        style.configure("TLabel", padding=10, font=('Arial', 12), background='#ecf0f1')
        style.configure("TEntry", padding=10, font=('Arial', 12))

        # System name label with bold and styling
        system_name_label = ttk.Label(master, text="Text to Speech Converter System", style="Bold.TLabel")
        system_name_label.pack(pady=(20, 50))

        self.label = ttk.Label(master, text="Enter the text you want to convert:", style="TLabel")
        self.label.pack()

        self.text_entry = ttk.Entry(master, width=50, style="TEntry")
        self.text_entry.pack(pady=10)

        self.convert_button = ttk.Button(master, text="Convert", command=self.convert_text, style="TButton")
        self.convert_button.pack(pady=10)

        # Converted text label
        self.converted_text_label = ttk.Label(master, text="", style="TLabel")
        self.converted_text_label.pack(pady=10)

        # Download button
        self.download_button = ttk.Button(master, text="Download Speech", command=self.download_audio, style="TButton")
        self.download_button.pack(pady=10)

        # Play button
        self.play_button = ttk.Button(master, text="Play Speech", command=self.play_audio, style="TButton")
        self.play_button.pack(pady=10)

        # Configure a style for the bold label
        style.configure("Bold.TLabel", foreground="#2ecc71", font=('Arial', 16, 'bold'))

    def convert_text(self):
        input_text = self.text_entry.get()
        if input_text:
            converted_text, audio_filename = self.text_to_speech(input_text)
            self.converted_text_label.config(text=converted_text)
            self.audio_filename = audio_filename

    def download_audio(self):
        if hasattr(self, 'audio_filename') and self.audio_filename:
            save_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
            if save_path:
                os.rename(self.audio_filename, save_path)
            else:
                os.system(f"start {self.audio_filename}")

    def play_audio(self):
        if hasattr(self, 'audio_filename') and self.audio_filename:
            pygame.mixer.init()
            pygame.mixer.music.load(self.audio_filename)
            pygame.mixer.music.play()

    def text_to_speech(self, text, language='en'):
        tts = gTTS(text=text, lang=language, slow=False)
        audio_filename = f"output_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp3"
        tts.save(audio_filename)
        return text, audio_filename

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(background='#ecf0f1')  # Set background color
    app = TextToSpeechApp(root)
    root.mainloop()
