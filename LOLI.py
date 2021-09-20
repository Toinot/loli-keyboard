# Créé par toinot.gury, le 20/09/2021 en Python 3.7
# Import Module
from tkinter import *
from tkhtmlview import HTMLLabel

# Create Object
root = Tk()
root.title("LOLI Keyboard")

# Set Geometry
root.geometry("1000x500")
root.resizable(width=False, height=False)
root.iconbitmap('LOLI.ico')

# Add label
my_label = HTMLLabel(root, html="""
        <h1>GEEKSFORGEEKS</h1>
        <h2>GEEKSFORGEEKS</h2>
        <h3>GEEKSFORGEEKS</h3>
        <h4>GEEKSFORGEEKS</h4>
        <h5>GEEKSFORGEEKS</h5>
        <h6>GEEKSFORGEEKS</h6>
    """)

# Adjust label
my_label.pack(pady=20, padx=20)

# Execute Tkinter
root.mainloop()
