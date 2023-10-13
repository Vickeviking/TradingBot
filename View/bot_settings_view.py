from tkinter import LabelFrame

class bot_settings_veiw(LabelFrame):
    def __init__(self, master=None, text="settings", bg="black"):
        super().__init__(master, text=text, bg=bg)
        self.master = master

    # Add any additional methods or configurations as needed