import datetime

from matplotlib import pyplot as plt
from tkinter import *
from tkinter import messagebox
import yfinance as yf
import numpy as np


root = Tk()
root.title('PlotIt')
root.geometry('200x60')

e = Entry(root, width=50)
e.pack()

# do umieszczenia rekomendacji na wykresie potrzebowalem wspolrzednych y dla kazdej
# daty rekomendacji. Funkcja jako argument przyjmuje daty rekomendacji, zmienia
# je do formatu takiego jak w danych hostorycznych (czyli ustawią czas na 00:00:00) i zwraca
# wartosci "Close" z danych historycznych
def getCloseOfIndex(dateList):
    myList = []
    for date in dateList:
        removeTime = datetime.datetime(date.year, date.month, date.day)
        try:
            getClose= hist[hist.index == removeTime]["Close"].values[0]
        except:
            getClose = 0
        myList.append(getClose)
    return myList

def graph():
    try:
        #pobiera ticker z inputu
        myTicker = yf.Ticker(e.get())
        
        global hist
        hist = myTicker.history(period="max")

        # pobiera rekomendacje, a jesli ich nie ma wyświetla komunikat
        recomm = myTicker.recommendations
        try:
            yValues = getCloseOfIndex(recomm.index)
        except:
            print("There is no recommendations!")
        
        # rysowanie wykresu
        plt.figure(figsize=(12,6))
        plt.plot(hist.index, hist["Close"], linewidth=0.5, c="#0f7791")
        plt.xlabel("Time")
        plt.ylabel("Close Position")
        plt.title("Company: " + e.get().upper())
        try:
            plt.scatter(recomm.index, yValues, s=1.2, c="red")
        except:
            print("There is no recommendations!")
        plt.show()
    except:
        messagebox.showinfo("Alert", "No data found")

my_button = Button(root, text="DO IT!", command=graph)
my_button.pack()



root.mainloop()