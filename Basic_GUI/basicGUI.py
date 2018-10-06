# is All Library (tkinter packageAll GUI Python)
from tkinter import * 
from tkinter import ttk


def helloworld():
	print('hello This is Diamond shop')


def calculate():
	price = 85000 # Diamond Price:
	quan = int(quantity.get()) # defualt of .get() is string
	total = price * quan
	print("Quantity of Diamond : %d Total Payment : %d Baht"%(quan,total))

#set GUI	
GUI = Tk()
GUI.geometry('500x500')
GUI.title('Peter Diamond Shop')

Title = Label(GUI,text='Quantity of Diamond', font=('Angsana New',18,'bold'))
Title.pack(padx=10, pady=10)
quantity = StringVar()



TextBox1 = ttk.Entry(GUI,textvariable=quantity,font=('Angsana New',18,'bold'))
TextBox1.pack(padx=10, pady=10)

B1 = ttk.Button(GUI,text='<<กดเลย>>',command=calculate)
B1.pack(padx=10, pady=10, ipadx=20, ipady=20)

GUI.mainloop()