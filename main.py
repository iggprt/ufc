
import os
from bs4 import BeautifulSoup
import re
import HTMLParser
import Tkinter as tk
import ttk

import matplotlib

files = os.listdir('./page_sources/fighters_stats/')
#pages = [ BeautifulSoup( open('./htmls/'+file, 'r').read(),'html.parser') for file in files ]

LARGE_FONT = ('Verdana', 8)

class UFC(tk.Tk):
	
	def __init__(self, *args, **kwargs):
	
		tk.Tk.__init__(self, *args, **kwargs)
		
		tk.Tk.wm_title(self, 'Solo de chitara')
		
		container = tk.Frame(self)		
		container.pack(side='top', fill='both', expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		
		self.frames = {}
		
		for F in (StartPage, PageOne, PageTwo):
		
			frame = F(container, self)
			self.frames[F] = frame			
			frame.grid (row=0, column = 0, sticky = 'nsew')
		
		self.show_frame(StartPage)
		
	def show_frame(self, cont):
		
		frame = self.frames[cont]
		frame.tkraise()
		
class StartPage(tk.Frame):
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='start page', font = LARGE_FONT)
		label.pack(pady=10, padx=10)
		
		button1 = tk.Button(self, text = '>', command = lambda: controller.show_frame(PageOne))
		button1.pack(side='right')
		
		button2 = tk.Button(self, text = '<', command = lambda: controller.show_frame(PageTwo))
		button2.pack(side='left')

class PageOne(tk.Frame):
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='page unos', font = LARGE_FONT)
		label.pack(pady=10, padx=10)
		
		button1 = tk.Button(self, text = '>', command = lambda: controller.show_frame(PageTwo))
		button1.pack(side='right')
		
		button2 = tk.Button(self, text = '<', command = lambda: controller.show_frame(StartPage))
		button2.pack(side='left')


class PageTwo(tk.Frame):
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='page dos', font = LARGE_FONT)
		label.pack(pady=10, padx=10)
		
		button1 = tk.Button(self, text = '>', command = lambda: controller.show_frame(StartPage))
		button1.pack(side='right')
		
		button2 = tk.Button(self, text = '<', command = lambda: controller.show_frame(PageOne))
		button2.pack(side='left')
		
app = UFC()
app.mainloop()