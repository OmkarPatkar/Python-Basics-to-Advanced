#importing the libraries:
from tkinter import Label, Tk
import time

# create window object and set size, and resaize property of the window
app_window = Tk()
app_window.title('Digital Clock')
app_window.geometry('480x150')
app_window.resizable(1,1)

#set font, background, foreground, and width of the text
text_font = ('Boulder', 65, 'bold')
background = '#f2e750'
foreground = '#363529'
border_width = 23

#combine all together
label = Label(app_window, font = text_font, bg = background, fg = foreground, bd = border_width)
label.grid(row = 0, column = 1)

#call the time method and set it in our window
def digital_clock():
    time_live = time.strftime('%H:%M:%S')
    label.config(text = time_live)
    label.after(200, digital_clock)

#call the function
digital_clock()
app_window.mainloop()