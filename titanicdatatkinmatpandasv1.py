import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

class TitanicApp:
    def __init__(self, master):
        self.master = master
        master.title("Titanic Data Explorer")

        # Button to show survival graph
        self.graph_button = tk.Button(master, text="Show Survival Graph", command=self.show_graph)
        self.graph_button.pack(pady=10)

        # Load the data
        self.data = pd.read_csv('/home/gandalf/Desktop/titanic.csv')  # <-- change path if needed

    def show_graph(self):
        # Count survivors vs non-survivors
        survival_counts = self.data['Survived'].value_counts()

        # Make a bar graph
        plt.bar(['Did Not Survive', 'Survived'], survival_counts)
        plt.title('Titanic Survival Counts')
        plt.xlabel('Outcome')
        plt.ylabel('Number of People')
        plt.show()

root = tk.Tk()
app = TitanicApp(root)
root.mainloop()
