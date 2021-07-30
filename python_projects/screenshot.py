"""
install libraries:
pip install pyautogui tk

run the program:
python screenshot.py
"""

# import libraries
import time
import pyautogui as ss
import tkinter as tk

# define a function to take screenshot
def screenshot():
    # generate random name
    name = int(round(time.time() * 1000))
    name = f'{name}.png'
    img = ss.screenshot(name)
    img.show()
    print('File saved!')

# create gui for our program
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# add buttons
button = tk.Button(
    frame,
    text = 'Take Screenshot',
    command = screenshot)
button.pack(side = tk.LEFT)

close = tk.Button(
    frame,
    text = 'QUIT',
    command = quit)
close.pack(side = tk.RIGHT)

root.mainloop()