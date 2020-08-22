from matplotlib import pyplot as plt
from tkinter import *
import yfinance as yf



root = Tk()
root.title('VIEW 1')
root.geometry('400x200')

#msft = yf.Ticker("MSFT")

#hist = msft.history(period="max")
#closing_pos = hist["Close"]



#print(msft.recommendations)
e = Entry(root, width=50)
e.pack()

def graph():
    myTicker = yf.Ticker(e.get())
    hist = myTicker.history(period="max")
    plt.plot(hist.index, hist["Close"])
    plt.show()

my_button = Button(root, text="DO IT!", command=graph)
my_button.pack()



root.mainloop()