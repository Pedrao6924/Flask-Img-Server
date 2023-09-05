import tkinter as tk
import ttkbootstrap as ttkb
from tkinter import filedialog

class Main:

    def __init__(self, root):

        self.root = root

        self.root.geometry("550x30")
        self.root.resizable(0, 0)
        self.root.title("Media Merger")
        style = ttkb.Style(theme='darkly')


        self.root.columnconfigure(20, weight=1, pad=20)
        self.root.columnconfigure(5, weight=3, pad=20)
        canvas = tk.Canvas(self.root)

        mediaLocation = tk.Label(self.root, text="Directory:")
        mediaLocation.grid(column=0, row=1, pady=5, padx=5,sticky="w")

        self.manga_dir = tk.StringVar()
        link = tk.Entry(self.root, width=50, textvariable=self.manga_dir)
        link.grid(column=1, row=1, pady=5, padx=5, sticky="w")

        findFolder = tk.Button(self.root, text="Img Location")
        findFolder.grid(column=3, row=1, padx=5, pady=5, sticky="w")

        startServer = tk.Button(self.root, text="Start Server")
        startServer.grid(column=4, row=1, padx=5, pady=5, sticky="w")

        #self.manga_dir.trace_add("write", gui.on_manga_dir_change(self.manga_dir, merge))

        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()
