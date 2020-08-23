import datetime
from matplotlib import pyplot as plt
from tkinter import *
import yfinance as yf
import numpy as np




root = Tk()
root.title('VIEW 1')
root.geometry('300x100')

msft = yf.Ticker("MSFT")

hist = msft.history(period="max")
#closing_pos = hist["Close"]
print(hist.index)
#msft = yf.Ticker("MSFT")
print(msft.recommendations)

#print(msft.recommendations)
e = Entry(root, width=50)
e.pack()
def getCloseOfIndex(dateList):
    myList = []
    for date in dateList:
        myVar = datetime.datetime(date.year, date.month, date.day)
        try:
            myList.append(hist[hist.index == myVar]["Close"].values[0])
        except:
            myList.append(0)
    #for date in datelist2:
        #print(hist[hist.index == date]["Close"])
       # myList.append(hist[hist.index == date]["Close"])
    return myList

def graph():
    myTicker = yf.Ticker(e.get())
    hist = myTicker.history(period="max")
    recomm = myTicker.recommendations
    yValues = getCloseOfIndex(recomm.index)
    print(type(yValues[0]))
    print(type(np.zeros(len(recomm))[0]))
    print((np.zeros(len(recomm))).shape)
    plt.plot(hist.index, hist["Close"])
    plt.scatter(recomm.index, yValues, s=1, c="red")
    plt.show()

my_button = Button(root, text="DO IT!", command=graph)
my_button.pack()



root.mainloop()