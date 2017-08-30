# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 11:59:11 2017

@author: vabattee
"""
##### Header for importing modules, etc #####
# Tkinter imports
import tkinter as tk
from tkinter import ttk

# MatPlotLib imports
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import style
import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

#Other imports
import urllib
import json
import pandas as pd
import numpy as np
import datetime as dt

##### End Header #####


#Styles
Large_Font = ("Verdana", 12)
style.use("ggplot") #, "dark_background")
pd.options.mode.chained_assignment = None

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)


def animatebtc(i): ### Currently useing BTC-e exchange, which is dead. Will have to update later.
    
    """
    These are alternative API links
    api_link = "https://www.bitstamp.net/api/v2/ticker/btcusd/"
    api_link = "https://btc-e.com/api/3/trades/btc_usd?limit=2000
    """
    
    api_link = "https://api.coindesk.com/v1/bpi/currentprice.json"
    
    data =  urllib.request.urlopen(api_link)
    data = data.read().decode("utf-8")
    data = json.loads(data)
    #df1 = data
    #print(df1)
    #data = data['bpi']
    data = pd.DataFrame(data, index = [0])
    data['timestamp'] = dt.datetime.now()
    
    """ 
    This will change as soon as I get my DataFrame above sorted out.
    USD_rate = data['USD']['rate_float']
    USD_time = data['USD']['rate_float']
    
    a.clear()
    
    a.plot_date(USD_time, USD_rate)
    """
            



class BTCStreamApp(tk.Tk): #adding tk.Tk allows the class to inherit the methods from tkinter inside the class
    
    def __init__(self, *args, **kwargs): #as "init", this will ALWAYS run when the class is called. This is a method, not merely a function.
        
        tk.Tk.__init__(self, *args, **kwargs)
        
#        tk.Tk.iconbitmap(self, default="C:\Users\IBM_ADMIN\Downloads\ancapstore_a_hm1_icon.ico") # *** Use the filepath - must be a *.ico that is 16x16 -- use GIMP
        tk.Tk.wm_title(self, "BTC Stream Client")        


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand= True)
        container.grid_rowconfigure(0, weight=1) #Number is the size, weight is the Priority
        container.grid_columnconfigure(0, weight=1)
        
        self.frames =  {}
        
        my_frames = [StartPage, PageOne, BTC_Page]
        
        for F in (my_frames):
                 
        
            frame = F(container, self)
            
            self.frames[F] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")
            
        
        self.show_frame(StartPage)
        
        
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()

     
        
class StartPage(tk.Frame): #Creating the basic start page on initialization
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("""Beta Testing Agreement and Disclaimer: 
            This product is intended for development use only. 
            Cryptocurrency prices herein may not reflect current or actual market data. 
            Use at your own risk"""), font=Large_Font)
        label.pack(pady=10,padx=10) #adds padding to the pack so it looks nicer
        
        button1 = ttk.Button(self, text = "Agree", 
                            command = lambda:controller.show_frame(BTC_Page))
        button1.pack()
        
        button2 = ttk.Button(self, text = "Disagree", 
                            command = quit())
        button2.pack()
        
        
        
class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #label_text = animatebtc(data) *** Probably just remove this
        label = tk.Label(self, text= "Page 1", font=Large_Font)
        label.pack(pady=10,padx=10)
        
        
        button1 = ttk.Button(self, text = "Disclaimer", 
                            command = lambda:controller.show_frame(StartPage))
        button1.pack()
        
        button2 = ttk.Button(self, text = "BTC Graph", 
                            command = lambda:controller.show_frame(BTC_Page))
        button2.pack()
        
        

        
class BTC_Page(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="BTC Price Graph", font=Large_Font)
        label.pack(pady=10,padx=10) 
        
        button1 = ttk.Button(self, text = "Disclaimer", 
                            command = lambda:controller.show_frame(StartPage))
        button1.pack()
        
        button2 = ttk.Button(self, text = "Visit Page 1", 
                            command = lambda:controller.show_frame(PageOne))
        button2.pack()
        
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



"""
Add a new page to the app by using the following code, then add what you want to the page:

class PAGENAME(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)        
"""




app = BTCStreamApp()
ani = animation.FuncAnimation(f, animatebtc, interval=1000) #interval is in milliseconds
app.mainloop()

        
        
        
        
      





















  
        
