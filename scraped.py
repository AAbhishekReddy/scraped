from tkinter import *
from tkinter import messagebox
import helper


mw = Tk()
mw.geometry('379x80')
mw.title("Scraped")


def send():
	if helper.scrap(e1.get(), e2.get()):
		messagebox.showinfo('Message','Done')
		e1.delete(0, 'end')
		e2.delete(0, 'end')

lb = Label(mw, text='Enter the Url here ---->')
lb.grid(row = 0, column = 0)
e1 = Entry(mw, bd = 3)
e1.focus()
e1.grid(row = 0, column = 1)
Label(mw, text='Enter the file destination here ---->').grid(row = 1, column = 0)
e2 = Entry(mw, bd = 3)
e2.grid(row = 1, column = 1)

butt = Button(mw, text='Submit', width = 25, command = send)
butt.grid(row = 2, column = 0)
but = Button(mw, text='Exit', width = 25, command = mw.destroy)
but.grid(row = 2, column = 1)

mw.mainloop()
