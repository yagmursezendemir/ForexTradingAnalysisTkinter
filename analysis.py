#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 17:36:05 2020

@author: yagmursezendemir
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import pandas as pd 
import numpy as np


window = tk.Tk()
window.geometry('1080x640')
window.title('Forex Trading')

pw = ttk.Panedwindow(window,orient = tk.HORIZONTAL ) 
pw.pack(fill = tk.BOTH, expand = True)

w2 = ttk.Panedwindow(pw, orient = tk.VERTICAL)

frame1 = ttk.Frame(pw, width = 360 , height = 640, relief = tk.SUNKEN)
frame2 = ttk.Frame(pw, width = 720 , height = 400, relief = tk.SUNKEN)
frame3 = ttk.Frame(pw, width = 720 , height = 240, relief = tk.SUNKEN)
#%%
w2.add(frame2)
w2.add(frame3)

pw.add(w2)
pw.add(frame1)


# frame1 treeview , open trade button
item = ''
def callback(event):
    global item
    item = treeview.identify('item', event.x , event.y)
    #print('Clicked: ' , item)
treeview = ttk.Treeview(frame1)
treeview.grid(row = 0 , column = 1,padx = 25 , pady = 25)
treeview.insert('', '0','Major', text = 'Major')
treeview.insert('Major','1','EUR/USD', text = 'EUR/USD')
treeview.insert('', '2','Minor', text = 'Minor')
treeview.insert('Minor','3','EUR/GBR', text = 'EUR/GBR')

treeview.bind('<Double-1>',callback)
# treeview button

def readNews(item):
    if item == 'EUR/USD':
        news = pd.read_csv('news_EURUSD.txt')
    elif item == 'EUR/GBR':
        news = pd.read_csv('news_EURGBR.txt')
    textBox.insert(tk.INSERT,news)
def openTrade():
    global data , future , line, canvas, data_close_array, future_array , ax1 , line2 , canvas2, ax2 , line3, canvas3, ax3,line3,canvas4,ax4
    print('Open_trade')
    if item != "":
        print('Chosen item: ' , item)
        if item == 'EUR/USD':
                
            #button settings
            open_button.config(state = 'disabled')
            start_button.config(state = 'normal') #
            #read data
            data = pd.read_csv('eurusd.csv')
            
            # split data
            future = data[-1000:]
            data = data[:len(data)-1000]
            data_close_array = data.close1.values
            future_array = list(future.close1.values)
            
            #line
            fig1 = plt.Figure(figsize = (5,4), dpi = 100)
            ax1 = fig1.add_subplot(111)
            line, = ax1.plot(range(len(data)), data.close1, color = 'blue')
            canvas = FigureCanvasTkAgg(fig1, master = tab1)
            canvas.draw()
            canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)
            
            #scatter
            fig2 = plt.Figure(figsize = (5,4), dpi = 100)
            ax2 = fig2.add_subplot(111)
            line2 = ax2.scatter(range(len(data)), data.close1,s = 1, alpha = 0.5, color = 'blue')
            canvas2 = FigureCanvasTkAgg(fig1, master = tab2)
            canvas2.draw()
            canvas2.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True) 
            
            #read news
            readNews(item)
        elif item == 'EUR/GBR':
                
            #button settings
            open_button.config(state = 'disabled')
            start_button.config(state = 'normal') #
            #read data
            data = pd.read_csv('eurgbr.csv')
            
            # split data
            future = data[-1000:]
            data = data[:len(data)-1000]
            data_close_array = data.close1.values
            future_array = list(future.close1.values)
            
            #line
            fig3 = plt.Figure(figsize = (5,4), dpi = 100)
            ax3 = fig3.add_subplot(111)
            line3, = ax3.plot(range(len(data)), data.close1, color = 'blue')
            canvas3 = FigureCanvasTkAgg(fig3, master = tab1)
            canvas3.draw()
            canvas3.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)
            
            #scatter
            fig4 = plt.Figure(figsize = (5,4), dpi = 100)
            ax4 = fig4.add_subplot(111)
            line4 = ax4.scatter(range(len(data)), data.close1,s = 1, alpha = 0.5, color = 'blue')
            canvas4 = FigureCanvasTkAgg(fig4, master = tab2)
            canvas4.draw()
            canvas4.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)
                        
            #read news
            readNews(item)
        else:
            messagebox.showinfo(title = 'Warning ' , message = 'Double click to choose currency pair')
    else:
        messagebox.showinfo(title = 'Warning ' , message = 'Double click to choose currency pair')

        
        
open_button = tk.Button(frame1, text = 'Open Trading', command = openTrade, fg = 'blue')
open_button.grid(row = 2 , column = 1 , padx = 5 , pady = 5)


# frame3  - text editor (fundemantal analysis) , scrollbar

textBox = tk.Text(frame3, width = 70 , height = 10, wrap = 'word')
textBox.grid(row = 0 , column = 0 , padx = 25 , pady  = 25)
scroll = tk.Scrollbar(frame3, orient = tk.VERTICAL , command = textBox.yview)
scroll.grid(row = 0 , column = 1 , sticky = tk.N + tk.S , pady = 10 )
textBox.config(yscrollcommand = scroll.set)

#frame2 tabview - radiobutton - button - result(labelframe) - plot 

tabs = ttk.Notebook(frame2, width = 540 , height = 300)
tabs.place(x = 25 , y = 25)

tab1 = ttk.Frame(tabs, width = 50 , height = 50)
tab2 = ttk.Frame(tabs)

tabs.add(tab1 , text = 'Line')
tabs.add(tab2, text = 'Scatter' , compound = tk.LEFT)

#radio button
method = tk.StringVar()
tk.Radiobutton(frame2, text = 'm1: ', value = 'm1' , variable = method).place(x = 600 , y = 100)
tk.Radiobutton(frame2, text = 'm2: ', value = 'm2' , variable = method).place(x = 600 , y = 125)


# label frame

label_frame = tk.LabelFrame(frame2, text = 'Result' , width = 100 , height = 150)

label_frame.place(x = 600, y = 25)
tk.Label(label_frame, text = 'Buy: ' , bd = 3 ).grid(row = 0 , column = 0 )
tk.Label(label_frame, text = 'Sell: ' , bd = 3 ).grid(row = 1 , column = 0 )

buy_value = tk.Label(label_frame, text = '1', bd=3)
buy_value.grid(row = 0 , column = 1)
sell_value = tk.Label(label_frame, text = '0', bd=3)
sell_value.grid(row = 1 , column = 1)

def moving_average(a, n=50):
    ret = np.cumsum(a,dtype = float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n-1:]/n #average 
    
def update():
    global data_close_array , ax1, ax2,ax3,ax4,ax4
    spread = 0.0002 #random
    buy_value.config(text = str((data_close_array[-1]-spread).round(5)))
    sell_value.config(text = str((data_close_array[-1]+spread).round(5)))
    
    window.after(500,update)
    data_close_array = np.append(data_close_array,future_array.pop(0))
    
    if method.get() == 'm1':
        if item == 'EUR/USD':
            #line plot
            ax1.set_xlim(0,len(data_close_array)+ 10)
            line.set_ydata(data_close_array)
            line.set_xdata(range(len(data_close_array)))
            
            #scatter plot
            ax2.set_xlim(0,len(data_close_array)+10)
            ax2.scatter(range(len(data_close_array)),data_close_array, s= 1,alpha = 0.5,color = 'blue')
            #moving average
            
            n = 50 # window size
            mid_rolling =moving_average(data_close_array,n)
            ax1.plot(range(n-1,len(data_close_array)),mid_rolling,linestyle = "--", color = 'red') 
            ax2.plot(range(n-1,len(data_close_array)),mid_rolling,linestyle = "--",  color = 'red') 
            canvas.draw()
            canvas2.draw()
            
        elif item == 'EUR/GBR':
            #line plot
            ax3.set_xlim(0,len(data_close_array)+ 10)
            line3.set_ydata(data_close_array)
            line3.set_xdata(range(len(data_close_array)))
            
            #scatter plot
            ax4.set_xlim(0,len(data_close_array)+10)
            ax4.scatter(range(len(data_close_array)),data_close_array, s= 1,alpha = 0.5,color = 'blue')
            #moving average
            
            n = 50 # window size
            mid_rolling =moving_average(data_close_array,n)
            ax3.plot(range(n-1,len(data_close_array)),mid_rolling,linestyle = "--", color = 'red') 
            ax4.plot(range(n-1,len(data_close_array)),mid_rolling,linestyle = "--",  color = 'red') 
            canvas3.draw()
            canvas4.draw()
    elif method.get() == 'm2':
        if item == 'EUR/USD':
            #line plot
            ax1.set_xlim(0,len(data_close_array)+ 10)
            line.set_ydata(data_close_array)
            line.set_xdata(range(len(data_close_array)))
            
            #scatter plot
            ax2.set_xlim(0,len(data_close_array)+10)
            ax2.scatter(range(len(data_close_array)),data_close_array, s= 1,alpha = 0.5,color = 'blue')
            #moving average
            
            n = 50 # window size
            mid_rolling =moving_average(data_close_array,n)
            ax1.plot(range(n-1,len(data_close_array)),mid_rolling,linestyle = "--", color = 'red') 
            ax2.plot(range(n-1,len(data_close_array)),mid_rolling,linestyle = "--",  color = 'red') 
            canvas.draw()
            canvas2.draw()
            
        elif item == 'EUR/GBR':
            #line plot
            ax3.set_xlim(0,len(data_close_array)+ 10)
            line3.set_ydata(data_close_array)
            line3.set_xdata(range(len(data_close_array)))
            
            #scatter plot
            ax4.set_xlim(0,len(data_close_array)+10)
            ax4.scatter(range(len(data_close_array)),data_close_array, s= 1,alpha = 0.5,color = 'blue')
            #moving average
            
            n = 200 # window size
            long_rolling =moving_average(data_close_array,n)
            ax3.plot(range(n-1,len(data_close_array)),long_rolling,linestyle = "--", color = 'green') 
            ax4.plot(range(n-1,len(data_close_array)),long_rolling,linestyle = "--",  color = 'green') 
            canvas3.draw()
            canvas4.draw()
    else:
        if item == 'EUR/USD':
            #line plot
            ax1.set_xlim(0,len(data_close_array)+ 10)
            line.set_ydata(data_close_array)
            line.set_xdata(range(len(data_close_array)))
            
            #scatter plot
            ax2.set_xlim(0,len(data_close_array)+10)
            ax2.scatter(range(len(data_close_array)),data_close_array, s= 1,alpha = 0.5,color = 'blue')

            

            canvas.draw()
            canvas2.draw()    
        elif item == 'EUR/GBR':
            #line plot
            ax3.set_xlim(0,len(data_close_array)+ 10)
            line3.set_ydata(data_close_array)
            line3.set_xdata(range(len(data_close_array)))
            
            #scatter plot
            ax4.set_xlim(0,len(data_close_array)+10)
            ax4.scatter(range(len(data_close_array)),data_close_array, s= 1,alpha = 0.5,color = 'blue')

            canvas3.draw()
            canvas4.draw()
        
            
def startTrading():
    window.after(0,update)
    print('start trading')
 #button  
start_button = tk.Button(frame2, text = 'Start Trading' , command = startTrading )
start_button.place(x = 600 , y = 150)
start_button.config(state = 'disabled')




window.mainloop()