from tkinter import LabelFrame

class live_stocks_veiw(LabelFrame):
    def __init__(self, master=None, text="live stocks", bg="green"):
        super().__init__(master, text=text, bg=bg)
        self.master = master

    # Add any additional methods or configurations as needed