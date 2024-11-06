from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import *

win = Tk()
win.geometry("600x600")
win.config(bg = 'gray')
win.title('Paint')

var1 = StringVar()
ms1 = Message(win, textvariable = var1, relief = RAISED, width=600, bd = 5, cursor = 'heart')
ms1.config(font = ('mitra', 12), pady=5, bg = 'white', fg = 'black')
ms1.pack(anchor = N, pady=(10, 5))
var1.set('This is a simple Paint window that created by farshad257\nEmail: farshadtfgh@gamil.com\nHelp :\nClick Left Mouce and Drag to draw Point\nClick Right Mouce and drag to draw Rectangle\nClick the Cursor and drag it to draw Triangle')

outline_color = 'black'
fill_color = 'white'

def getcolor(is_fill=False):
    global outline_color, fill_color
    color = askcolor()[1]
    if is_fill:
        fill_color = color
    else:
        outline_color = color
    
frame_buttons = Frame(win, bg = 'gray')
frame_buttons.pack(anchor = N, pady = (5, 5))

btn_outline = ttk.Button(frame_buttons, text = 'Outline Color', command = lambda: getcolor(is_fill = False))
btn_fill = ttk.Button(frame_buttons, text = 'Fill Color', command = lambda: getcolor(is_fill = True))
style = ttk.Style()
style.theme_use('alt')
style.configure('TButton', font=('American typewriter', 14), background='#232323', foreground='white')
style.map('TButton', background=[('active', '#ff0000')])

btn_outline.pack(side  = LEFT, padx = 10)
btn_fill.pack(side = RIGHT, padx = 10)



c_width = 500
c_height = 300
c = Canvas(win, width = c_width, height = c_height, bg = 'white')
c.pack(fill = 'both', expand = 1, pady = (10, 0))

def point(event):
	x1 = event.x - 1
	y1 = event.y - 1
	x2 = event.x + 1
	y2 = event.y + 1
	c.create_oval(x1,y1,x2,y2, fill = 'black')

def rectangle(event):
	x1 = event.x
	y1 = event.y
	x2 = event.x + 50
	y2 = event.y + 25

	c.create_rectangle(x1, y1, x2, y2, outline = outline_color, fill = fill_color, width = 2)

def triangle(event):
	x1 = event.x
	y1 = event.y
	x2 = event.x - 20
	y2 = event.y + 30
	x3 = event.x + 20
	y3 = event.y + 30
	c.create_polygon(x1, y1, x2, y2, x3, y3, outline = outline_color, fill = fill_color, width = 2)



c.bind('<B1-Motion>', point)
c.bind('<B2-Motion>', triangle)
c.bind('<B3-Motion>', rectangle)

win.mainloop()
