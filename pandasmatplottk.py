import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

class TemperatureApp:
    def __init__(self, master):
        self.master = master
        master.title("Temperature Viewer 🌡️")

        # Create Data
        self.data = {
            'City': ['New York', 'Los Angeles', 'Chicago', 'Miami', 'Seattle'],
            'Temperature': [75, 85, 70, 90, 65]
        }
        self.df = pd.DataFrame(self.data)

        # Label
        self.label = tk.Label(master, text="Click the button to show the temperature graph!")
        self.label.pack(pady=10)

        # Button
        self.show_button = tk.Button(master, text="Show Graph", command=self.show_graph)
        self.show_button.pack(pady=10)

    def show_graph(self):
        plt.figure(figsize=(8,5))
        plt.bar(self.df['City'], self.df['Temperature'], color='skyblue')
        plt.title('Average City Temperatures')
        plt.xlabel('City')
        plt.ylabel('Temperature (°F)')
        plt.tight_layout()
        plt.show()

# --- Main program
root = tk.Tk()
app = TemperatureApp(root)
root.mainloop()
