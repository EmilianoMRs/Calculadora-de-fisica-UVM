from tkinter import *

# Create the main window
root = Tk()

# Set a title for the window
root.title("Hello, World!")

# Create a label widget with the text "Hello, World!"
label = Label(root, text="Hello, World!")

# Pack the label widget onto the main window
label.pack()

# Start the main event loop to display the window
root.mainloop()