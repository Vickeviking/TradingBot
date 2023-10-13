from tkinter import LabelFrame

class bot_graph_veiw(LabelFrame):
    def __init__(self, master=None, text="Graph", bg="blue"):
        super().__init__(master, text=text, bg=bg)
        self.master = master

    # Add any additional methods or configurations as needed