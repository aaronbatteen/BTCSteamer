# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 19:13:48 2017

@author: vabattee
"""

####### Begin Header #######
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
#import gspread
#from gspread import sheets

#Styles and Misc Method Options
Large_Font = ("Verdana", 12)
style.use("ggplot") #, "dark_background")
pd.options.mode.chained_assignment = None



### Shorthand methods for matplotlib ###
f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)


####### End Header #######





def call_api_bitstamp(df):
    
    ### BTC Call ###
    btc_link = "https://www.bitstamp.net/api/v2/ticker/btcusd/"
    btc_data =  urllib.request.urlopen(btc_link)
    btc_data = btc_data.read().decode("utf-8")
    btc_data = json.loads(btc_data)
    print(btc_data)
    
    df_btc = pd.DataFrame(btc_data, index=['BTC_USD'])
    btc_data["datestamp"] = np.array(btc_data["timestamp"]).astype("datetime64[s]")
    btcDates = (btc_data['datestamp']).tolist()
    ### End BTC Call ###
    
    ### LTC Call ###
    ltc_link = "https://www.bitstamp.net/api/v2/ticker/ltcusd/"
    ltc_data =  urllib.request.urlopen(ltc_link)
    ltc_data = ltc_data.read().decode("utf-8")
    ltc_data = json.loads(ltc_data)
    print(ltc_data)
    
    df_ltc = pd.DataFrame(ltc_data, index=['LTC_USD'])
    ### End LTC Call ###
    
    ### Eth Call ###
    eth_link = "https://www.bitstamp.net/api/v2/ticker/ethusd/"
    eth_data =  urllib.request.urlopen(eth_link)
    eth_data = eth_data.read().decode("utf-8")
    eth_data = json.loads(eth_data)
    print(eth_data)
    
    df_eth = pd.DataFrame(eth_data, index=['ETH_USD'])
    ### Eth Call ###
    
    #df = [btc_data, ltc_data, eth_data]
    frames = [df_btc, df_ltc, df_eth]
    df = pd.concat(frames)
    
    return df

##### End call_api_bitstamp #####


df = []
df = df.append(call_api_bitstamp(df))

#print(df)




    
"""
df = []
#data_fr = call_api_coindesk(df)
data_fr = call_api_bitstamp(df)


#print(data)
"""