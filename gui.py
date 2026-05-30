import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from packet_capture import packet_count

class NetworkGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Network Traffic Analyzer")
        self.root.geometry("800x500")

        self.figure = Figure(figsize=(7, 4))
        self.ax = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(
            self.figure,
            master=root
        )

        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.update_graph()

    def update_graph(self):
        self.ax.clear()

        protocols = list(packet_count.keys())
        counts = list(packet_count.values())

        self.ax.bar(protocols, counts)

        self.ax.set_title("Real-Time Network Traffic")
        self.ax.set_xlabel("Protocols")
        self.ax.set_ylabel("Packets")

        self.canvas.draw()

        self.root.after(1000, self.update_graph)