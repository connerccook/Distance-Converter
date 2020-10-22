import tkinter as tk
from tkinter import ttk
import tkinter.font as font
try: #if the application is run on windows it looks nicer, but not on mac or linux
    from ctypes import wind11
    wind11.shcore.SetProcessDpiAwareness(1)
except :
    pass

root=tk.Tk()
root.title("Distance Converter")

font.nametofont("TkDefaultFont").configure(size=15)#changes font for all text except entry
#must change font within entry func 
style = ttk.Style(root)
print(style.theme_names())
print(style.theme_use("aqua"))

meters_value = tk.StringVar()
feet_value = tk.StringVar(value = "Feet shown here")

def calculate_feet(*args):
    try:
        meters = float(meters_value.get())
        feet = meters* 3.28084
        feet_value.set(f"{feet:.3f}") #feet:.3f is pretty much set precision. 3 is for 3 decimals, f is for floats
    except ValueError:
        pass

def quit_():
    root.destroy()
root.columnconfigure(0, weight=1) #this makes the root stay in the middle as it expands

main = ttk.Frame(root, padding=(30,15))
main.grid()

meters_label = ttk.Label(main, text="Meters:")
meters_input = ttk.Entry(main, width=10, textvariable=meters_value, font=("Segoe UI", 15))
meters_input.grid(row=0,column=1, sticky="EW", padx=5,pady=5)
meters_input.focus()
feet_label = ttk.Label(main, text="Feet:")
feet_display = ttk.Label(main, textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)
quit_button = ttk.Button(main, text="Quit", command=quit_)

meters_label.grid(row=0,column=0, sticky="W")
meters_input.grid(row=0,column=1, sticky="EW")
feet_label.grid(row=1,column=0, sticky="W")
feet_display.grid(row=1, column=1,sticky="EW")
calc_button.grid(row=2, column=0, columnspan=2, sticky="EW")#the button takes up two column spaces
quit_button.grid(row=3,column=0,columnspan=2, sticky="EW")

for child in main.winfo_children(): #applys padx and pady to all child(the things with grids) makes look better
    child.grid_configure(padx=15,pady=15)

root.bind("<Return>", calculate_feet)#this is a keybinding so that when user press enter, it "clicks" the calculate button
root.bind("<KP_Enter>", calculate_feet)
#root.bind("<Escape>", quit_)
root.mainloop()