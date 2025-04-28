import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TitanicDashboard:
    def __init__(self, master):
        self.master = master
        master.title("Titanic Dashboard")
        master.configure(bg="#2e2e2e")

        # Load Titanic CSV
        self.data = pd.read_csv('/home/gandalf/Desktop/titanic.csv')

        # Convert 'Survived' 0/1 into 'No'/'Yes'
        self.data['Survived'] = self.data['Survived'].map({0: 'No', 1: 'Yes'})

        # Main container (frame)
        self.main_frame = tk.Frame(master, bg="#2e2e2e")
        self.main_frame.pack(fill='both', expand=True)

        # LEFT - Treeview (Data list)
        self.tree_frame = tk.Frame(self.main_frame, bg="#2e2e2e")
        self.tree_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(self.tree_frame, columns=("Name", "Sex", "Age", "Survived"), show='headings')
        self.tree.pack(side='left', fill='both', expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Define columns
        self.tree.heading("Name", text="Name")
        self.tree.heading("Sex", text="Sex")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Survived", text="Survived")

        self.tree.column("Name", width=180)
        self.tree.column("Sex", width=80)
        self.tree.column("Age", width=60)
        self.tree.column("Survived", width=80)

        self.insert_data()

        # RIGHT - Graphs
        self.graph_frame = tk.Frame(self.main_frame, bg="#2e2e2e")
        self.graph_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10)

        self.create_graphs()

    def insert_data(self):
        for _, row in self.data.iterrows():
            self.tree.insert("", "end", values=(row["Name"], row["Sex"], row["Age"], row["Survived"]))

    def create_graphs(self):
        # Setup Matplotlib figure
        fig, axs = plt.subplots(2, 1, figsize=(5, 8))
        fig.patch.set_facecolor('#2e2e2e')
        fig.tight_layout(pad=4)

        # Graph 1: Survival Pie Chart
        survived_counts = self.data['Survived'].value_counts()
        axs[0].pie(
            survived_counts,
            labels=survived_counts.index,
            autopct='%1.1f%%',
            startangle=90,
            colors=["#4CAF50", "#F44336"]
        )
        axs[0].set_title('Survival Rate', color="white")
        
        # Graph 2: Age Histogram
        axs[1].hist(self.data['Age'].dropna(), bins=20, color="#2196F3", edgecolor="black")
        axs[1].set_title('Age Distribution', color="white")
        axs[1].set_xlabel('Age')
        axs[1].set_ylabel('Passengers')

        # Change text color to white
        for ax in axs:
            ax.title.set_color('white')
            ax.xaxis.label.set_color('white')
            ax.yaxis.label.set_color('white')
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')

        # Embed figure into Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = TitanicDashboard(root)
    root.mainloop()
