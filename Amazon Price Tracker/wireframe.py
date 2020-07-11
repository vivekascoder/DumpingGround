#!/usr/bin/python3
"""
Name: wireframe.py
Description: A interface for our application.
"""

from tkinter import *
from tkinter import ttk
import datetime
import threading
from time import sleep
from scraping import get_price

class Tracker(Tk):
	def __init__(self):
		super(Tracker, self).__init__()
		self.title("Amazon Price Tracker")
		self.minsize(640, 400)
		# self.resizable(False, False)
		self.drawUI()

	def drawUI(self):
		Label(self, text="Amazon Product Tracker", fg="white", bg="#333", width=58, justify=CENTER, font=("Arial", 15, "bold")).place(x=0, y=0)
		Label(self, text="Url of the product to track:").place(x=20, y=50)
		Label(self, text="Live tracking price:").place(x=400, y=50)
		self.url = Entry(self, width=38)
		self.url.place(x=20, y=70)
		ttk.Button(self, text="Track Price", command=lambda:threading.Thread(target=self.track_order, args=()).start()).place(x=20, y=100)
		self.history = ttk.Treeview(self, columns=('Time Stamp', 'Amazon Price'))
		self.history.place(x=20, y=150)
		self.history.heading('Time Stamp', text='Time Stamp')
		self.history.heading('Amazon Price', text='Amazon Price')
		# self.history.column('', width=2, anchor='center')
		# self.history.insert('', 'end', 'Amazon Price', text='Widget Tour')
		# self.history.insert('', 'end', text='Listbox', values=('15KB Yesterday mark'))
		# self.history.insert('', 'end', text='', values=("Hello World"))
		self.current_price_var = StringVar()
		self.current_price = Label(self, font=("Arial", 25, "bold"), textvariable=self.current_price_var, fg="red")
		self.current_price_var.set("00000")
		self.current_price.place(x=400, y=80)

	def track_order(self):
		# counter = 1
		while True:
			time = datetime.datetime.now()
			url = self.url.get()
			print(url)
			price = get_price(url)
			print(price)
			self.current_price_var.set(price)
			self.history.insert('', 'end', text="Tracking... ", values=(f"{time.ctime()}", str(price)))
			sleep(10)
		# counter +=1




tracker = Tracker()
tracker.mainloop()
