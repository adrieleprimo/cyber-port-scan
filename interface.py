import threading
import socket
import tkinter as tk
from tkinter import scrolledtext
from threadingScan import thread_scan

class portScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cyber Port Scan")
        self.root.geometry("600x400")

        self.ip_label = tk.Label(root, text="Enter IP Address:")
        self.ip_label.pack()

        self.ip_entry = tk.Entry(root)
        self.ip_entry.pack()

        self.scan_button = tk.Button(root, text="Start Scan")
        self.scan_button.pack()

        self.results_text = scrolledtext.ScrolledText(root, width=70, height=20)
        self.results_text.pack()

   

if __name__ == "__main__":
    root = tk.Tk()
    app = portScannerApp(root)
    root.mainloop()

