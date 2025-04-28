import tkinter as tk
from tkinter import ttk
import pandas as pd

class TitanicApp:
    def __init__(self, master):
        self.master = master
        master.title("Titanic Passenger Information")

        # Load Titanic data
        self.data = pd.read_csv('/home/gandalf/Desktop/titanic.csv')

        # Create a Frame
        frame = ttk.Frame(master, padding=10)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Create a Treeview widget inside the Frame
        self.tree = ttk.Treeview(frame)

        # Define columns
        self.tree['columns'] = ('Name', 'Sex', 'Age', 'Survived')

        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("Name", anchor=tk.W, width=200)
        self.tree.column("Sex", anchor=tk.CENTER, width=80)
        self.tree.column("Age", anchor=tk.CENTER, width=50)
        self.tree.column("Survived", anchor=tk.CENTER, width=80)

        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("Name", text="Name", anchor=tk.W)
        self.tree.heading("Sex", text="Sex", anchor=tk.CENTER)
        self.tree.heading("Age", text="Age", anchor=tk.CENTER)
        self.tree.heading("Survived", text="Survived", anchor=tk.CENTER)

        # Insert Data right hurr
        for index, row in self.data.iterrows():
            self.tree.insert("", tk.END, values=(row['Name'], row['Sex'], row['Age'], row['Survived']))

        # Add a Scrollbar, bro
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

root = tk.Tk()
app = TitanicApp(root)
root.mainloop()
