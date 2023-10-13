# Import the library tkinter 
from tkinter import *
  
app = Tk() 
app.title("Minute Trade Bot") 
app.geometry("2560x1600+0+0")
app.grid_columnconfigure(0, weight=355000)
app.grid_columnconfigure(1, weight=234375)
app.grid_columnconfigure(2, weight=441100)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
  
frame1 = LabelFrame(app, text="Fruit", bg="green") 
frame2 = LabelFrame(app, text="Vegetable", bg="yellow")
frame3 = LabelFrame(app, text="Vegetable", bg="blue")
frame4 = LabelFrame(app, text="Vegetable", bg="red")
  
# Displaying in frame
frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=0, column=1, sticky="nsew")
frame3.grid(row=0, column=2, sticky="nsew")
frame4.grid(row=1, column=0, columnspan=3, sticky="nsew")
  
# Make the loop for displaying app 
app.mainloop() 


