import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

class TitanicApp:
    def __init__(self, master):
        self.master = master
        master.title("Titanic Data Explorer")

        # Load the data
        self.data = pd.read_csv('/home/gandalf/Desktop/titanic.csv')

        # One button to show all graphs
        self.graph_button = tk.Button(master, text="Show All Graphs", command=self.show_all_graphs)
        self.graph_button.pack(pady=10)

    def show_all_graphs(self):
        fig, axs = plt.subplots(3, 1, figsize=(10, 12))  # 3 rows, 1 column

        # Graph 1: Survival counts
        survival_counts = self.data['Survived'].value_counts()
        axs[0].barh(['Did Not Survive', 'Survived'], survival_counts, color=['red', 'green'])
        axs[0].set_title('Titanic Survival Counts')
        axs[0].set_xlabel('Number of People')

        # Graph 2: Survival by Gender
        gender_survival = self.data.groupby('Sex')['Survived'].sum()
        axs[1].barh(gender_survival.index, gender_survival.values, color=['blue', 'pink'])
        axs[1].set_title('Survival by Gender')
        axs[1].set_xlabel('Number of Survivors')

        # Graph 3: Survival by Passenger Class
        class_survival = self.data.groupby('Pclass')['Survived'].sum()
        axs[2].barh(class_survival.index.astype(str), class_survival.values, color=['gold', 'silver', 'brown'])
        axs[2].set_title('Survival by Passenger Class')
        axs[2].set_xlabel('Number of Survivors')

        plt.tight_layout()  # Make sure nothing overlaps
        plt.show()

root = tk.Tk()
app = TitanicApp(root)
root.mainloop()
