import tkinter as tk

class MyFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        
        # Create widgets for your frame
        self.label = tk.Label(self, text="Hello, Tkinter!")
        self.label.pack()

        self.quit_button = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit_button.pack()

