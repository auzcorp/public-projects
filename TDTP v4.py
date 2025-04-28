import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt

class TitanicApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Titanic Data Viewer - Dark Mode")
        self.master.configure(bg="#2e2e2e")

        # Load Titanic dataset
        self.data = pd.read_csv('/home/gandalf/Desktop/titanic.csv')  # adjust your path if needed

        # Setup tabs
        self.tab_control = ttk.Notebook(self.master)
        self.dashboard_tab = tk.Frame(self.tab_control, bg="#2e2e2e")
        self.table_tab = tk.Frame(self.tab_control, bg="#2e2e2e")
        self.chart_tab = tk.Frame(self.tab_control, bg="#2e2e2e")

        self.tab_control.add(self.dashboard_tab, text="Dashboard")
        self.tab_control.add(self.table_tab, text="Table View")
        self.tab_control.add(self.chart_tab, text="Charts")
        self.tab_control.pack(expand=1, fill="both")

        self.create_dashboard()
        self.create_table()
        self.create_chart()

    def create_dashboard(self):
        label = tk.Label(self.dashboard_tab, text="Welcome to the Titanic Dashboard!", font=("Arial", 24), bg="#2e2e2e", fg="white")
        label.pack(pady=20)

        info = tk.Label(
            self.dashboard_tab,
            text="View survival stats, explore passengers, and analyze the data!",
            font=("Arial", 14),
            bg="#2e2e2e",
            fg="white"
        )
        info.pack()

    def create_table(self):
        # Frame for search and table
        search_frame = tk.Frame(self.table_tab, bg="#2e2e2e")
        search_frame.pack(fill=tk.X, pady=5)

        tk.Label(search_frame, text="Search Name:", bg="#2e2e2e", fg="white").pack(side=tk.LEFT, padx=5)
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, padx=5)
        search_entry.bind("<KeyRelease>", self.search_data)

        table_frame = tk.Frame(self.table_tab, bg="#2e2e2e", padx=10, pady=10)
        table_frame.pack(fill=tk.BOTH, expand=True)

        tree_scroll = ttk.Scrollbar(table_frame)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(table_frame, columns=("Name", "Sex", "Age", "Survived"), show="headings", yscrollcommand=tree_scroll.set)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Sex", text="Sex")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Survived", text="Survived")

        self.tree.column("Name", anchor=tk.W, width=200)
        self.tree.column("Sex", anchor=tk.CENTER, width=100)
        self.tree.column("Age", anchor=tk.CENTER, width=50)
        self.tree.column("Survived", anchor=tk.CENTER, width=80)

        self.tree.pack(fill=tk.BOTH, expand=True)
        tree_scroll.config(command=self.tree.yview)

        # Tag colors for survival
        self.tree.tag_configure('survived', background='lightgreen')
        self.tree.tag_configure('not_survived', background='lightcoral')

        self.load_data()

    def load_data(self, filter_text=""):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for _, row in self.data.iterrows():
            if filter_text.lower() in str(row['Name']).lower():
                survived_text = "Yes" if row['Survived'] == 1 else "No"
                tag = "survived" if survived_text == "Yes" else "not_survived"
                self.tree.insert("", tk.END, values=(row['Name'], row['Sex'], row['Age'], survived_text), tags=(tag,))

    def search_data(self, event):
        search_text = self.search_var.get()
        self.load_data(filter_text=search_text)

    def create_chart(self):
        chart_frame = tk.Frame(self.chart_tab, bg="#2e2e2e")
        chart_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Create three small charts side by side
        fig, axes = plt.subplots(1, 3, figsize=(12, 4))
        fig.patch.set_facecolor('#2e2e2e')

        # 1. Survival counts
        self.data['Survived'].replace({0: 'No', 1: 'Yes'}, inplace=True)
        self.data['Survived'].value_counts().plot(kind='bar', ax=axes[0], color=['red', 'green'])
        axes[0].set_title('Survived Count')

        # 2. Gender distribution
        self.data['Sex'].value_counts().plot(kind='bar', ax=axes[1], color=['blue', 'pink'])
        axes[1].set_title('Gender Count')

        # 3. Age distribution
        self.data['Age'].dropna().plot(kind='hist', bins=20, ax=axes[2], color='orange')
        axes[2].set_title('Age Distribution')

        plt.tight_layout()

        # Embed the Matplotlib figure into Tkinter
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = TitanicApp(root)
    root.mainloop()
