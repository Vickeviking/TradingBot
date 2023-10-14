from tkinter import LabelFrame

class bot_settings_veiw(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg="black"):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border= 0, borderwidth=0)

    # Add any additional methods or configurations as needed
    