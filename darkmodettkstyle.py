import tkinter as tk
from tkinter import ttk

class DarkModeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dark Mode TTK Interface")
        self.root.geometry("600x400")

        self.style = ttk.Style()
        self.set_dark_mode()

        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(fill='both', expand=True)

        self.label = ttk.Label(self.frame, text="Welcome to the Dark Mode GUI!", style="Dark.TLabel")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(self.frame, width=40)
        self.entry.pack(pady=10)

        self.button = ttk.Button(self.frame, text="Submit", command=self.on_submit)
        self.button.pack(pady=10)

        self.output = ttk.Label(self.frame, text="", style="Dark.TLabel")
        self.output.pack(pady=10)

    def set_dark_mode(self):
        self.root.configure(bg='#2e2e2e')
        self.style.theme_use('default')
        self.style.configure("TFrame", background="#2e2e2e")
        self.style.configure("TLabel", background="#2e2e2e", foreground="white")
        self.style.configure("TEntry", fieldbackground="#3c3f41", foreground="white")
        self.style.configure("TButton", background="#5c5c5c", foreground="white")
        self.style.map("TButton",
                       background=[('active', '#707070')],
                       foreground=[('active', 'white')])
        self.style.configure("Dark.TLabel", background="#2e2e2e", foreground="white")

    def on_submit(self):
        user_input = self.entry.get()
        self.output.config(text=f"You entered: {user_input}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DarkModeGUI(root)
    root.mainloop()