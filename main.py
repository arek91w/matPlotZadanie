import datetime
from matplotlib import pyplot as plt
from tkinter import *
import yfinance as yf
import numpy as np




root = Tk()
root.title('VIEW 1')
root.geometry('300x100')



#hist = msft.history(period="max")
#closing_pos = hist["Close"]
#print(hist.index)
#msft = yf.Ticker("MSFT")
#print(msft.recommendations)

#print(msft.recommendations)
e = Entry(root, width=50)
e.pack()
def getCloseOfIndex(dateList):
    myList = []
    print(hist)
    for date in dateList:
        myVar = datetime.datetime(date.year, date.month, date.day)
        try:
            xx = hist[hist.index == myVar]["Close"].values[0]
        except:
            xx = 0
        myList.append(xx)
    #for date in datelist2:
        #print(hist[hist.index == date]["Close"])
       # myList.append(hist[hist.index == date]["Close"])
    return myList

def graph():
    myTicker = yf.Ticker(e.get())
    global hist
    hist = myTicker.history(period="max")
    recomm = myTicker.recommendations
    yValues = getCloseOfIndex(recomm.index)
    print(recomm.index)
    print(yValues)
    plt.plot(hist.index, hist["Close"], linewidth=0.4)
    plt.scatter(recomm.index, yValues, s=0.9, c="red")
    plt.show()

my_button = Button(root, text="DO IT!", command=graph)
my_button.pack()



root.mainloop()