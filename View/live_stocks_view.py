from tkinter import LabelFrame

class live_stocks_veiw(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg="green"):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)

    # Add any additional methods or configurations as needed