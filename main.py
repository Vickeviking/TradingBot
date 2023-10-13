import tkinter as tk
from root_view import MyFrame  # Import the Frame class from the other file

def main():
    root = tk.Tk()
    root.title("Minute Trader Bot")
    root.geometry("2560x1600")

    # Create an instance of the frame from the other file
    frame = MyFrame(root)
    frame.pack()

    root.mainloop()

if __name__ == "__main__":
    main()



