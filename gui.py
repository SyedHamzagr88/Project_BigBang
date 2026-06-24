import tkinter as tk
import winsound
import time
from translator import text_to_morse, morse_to_text

DOT_DURATION = 200
DASH_DURATION = 600
FREQ = 800

class MorseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MORSE TRANSLATOR")
        self.root.geometry("600x400")
        self.root.config(bg="#1e1e1e")

        tk.Label(root, text="MORSE CODE TRANSLATOR", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="white").pack(pady=15)
        tk.Label(root, text="ENTER THE TEXT", bg="#1e1e1e", fg="white", font=("Arial", 11)).pack()

        self.input_entry = tk.Entry(root, font=("Arial", 13), width=40)
        self.input_entry.pack(pady=5)

        btn_frame = tk.Frame(root, bg="#1e1e1e")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="TEXT TO MORSE", command=self.convert_to_morse, bg="#4CAF50", fg="white", font=("Arial", 11), width=15).pack(side="left", padx=5)
        tk.Button(btn_frame, text="MORSE TO TEXT", command=self.convert_to_text, bg="#2196F3", fg="white", font=("Arial", 11), width=15).pack(side="left", padx=5)

        tk.Label(root, text="RESULT:", bg="#1e1e1e", fg="white", font=("Arial", 11)).pack(pady=(15, 0))

        self.output_label = tk.Label(root, text="", font=("Courier", 14), bg="#1e1e1e", fg="#00ff00", wraplength=500)
        self.output_label.pack(pady=10)

        tk.Button(root, text="🔊 Play Morse Sound", command=self.play_morse_sound, bg="#FF9800", fg="white", font=("Arial", 11), width=20).pack(pady=10)

        self.current_morse = ""

    def convert_to_morse(self):
        text = self.input_entry.get()
        self.current_morse = text_to_morse(text)
        self.output_label.config(text=self.current_morse)

    def convert_to_text(self):
        morse = self.input_entry.get()
        decoded = morse_to_text(morse)
        self.output_label.config(text=decoded)

    def play_morse_sound(self):
        if not self.current_morse:
            self.output_label.config(text="Convert text to Morse first!")
            return
        self.root.after(100, self._beep_sequence)

    def _beep_sequence(self):
        for symbol in self.current_morse:
            if symbol == '.':
                winsound.Beep(FREQ, DOT_DURATION)
            elif symbol == '-':
                winsound.Beep(FREQ, DASH_DURATION)
            elif symbol == ' ':
                time.sleep(0.2)
            elif symbol == '/':
                time.sleep(0.4)

if __name__ == "__main__":
    root = tk.Tk()
    app = MorseApp(root)
    root.mainloop()