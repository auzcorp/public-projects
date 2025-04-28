import tkinter as tk

class SandwichMaker:
    def __init__(self, master):
        self.master = master
        master.title("Sandwich Maker 🥪")

        self.plate = []

        self.label = tk.Label(master, text="Build your sandwich!")
        self.label.pack(pady=10)

        self.add_bread_button = tk.Button(master, text="Add Bread", command=self.add_bread)
        self.add_bread_button.pack(pady=5)

        self.add_cheese_button = tk.Button(master, text="Add Cheese", command=self.add_cheese)
        self.add_cheese_button.pack(pady=5)

        self.add_turkey_button = tk.Button(master, text="Add Turkey", command=self.add_turkey)
        self.add_turkey_button.pack(pady=5)

        self.add_lettuce_button = tk.Button(master, text="Add Lettuce", command=self.add_lettuce)
        self.add_lettuce_button.pack(pady=5)

        self.show_button = tk.Button(master, text="Show Sandwich", command=self.show_sandwich)
        self.show_button.pack(pady=10)

        self.sandwich_label = tk.Label(master, text="")
        self.sandwich_label.pack(pady=10)

    def add_bread(self):
        self.plate.append('Bread 🥖')

    def add_cheese(self):
        self.plate.append('Cheese 🧀')

    def add_turkey(self):
        self.plate.append('Turkey 🍗')

    def add_lettuce(self):
        self.plate.append('Lettuce 🥬')

    def show_sandwich(self):
        if not self.plate:
            self.sandwich_label.config(text="Your sandwich is empty!")
        else:
            sandwich = " + ".join(self.plate)
            self.sandwich_label.config(text=f"Your sandwich: {sandwich}")

# --- Main program
root = tk.Tk()
sandwich_maker = SandwichMaker(root)
root.mainloop()
