import tkinter as tk
import threading

from gui import NetworkGUI
from packet_capture import start_capture

capture_thread = threading.Thread(
    target=start_capture,
    daemon=True
)

capture_thread.start()

root = tk.Tk()

app = NetworkGUI(root)

root.mainloop()