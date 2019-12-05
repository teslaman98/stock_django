import requests
import pandas as pd
import json
import csv
import matplotlib.pyplot as plt
import numpy as np





def STONKS_csv():
    symbol = 'AAPL'
    interval = "5min"
    key = "high"
    API_key = "FGZ5VI2OU5B413FO"
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="+symbol+"&interval="+interval+"&outputsize=full&apikey="+API_key+"&datatype=csv"
    data_list = pd.read_csv(url)
    #data_list.set_index('timestamp', inplace = True)
    data_list['high'].plot()
    plt.legend()
    g = plt.show()
    return (g)
    #print (data_value)


STONKS_csv()

"""
csv = data_list
key = "high"

def stock_value(csv, key):
    data_value = csv[key]
    return data_value
    print (data_value)



AAPL = STONKS_csv("AAPL", '5min')

AAPL["high"].plot()
plt.legend()
plt.savefig('stock_png/AAPL.png')
"""