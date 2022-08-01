import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import plotly.graph_objects as go


# obtenha o preço de uma ação usando o Yahoo Finance com start_date e end_date
def get_stock_price(stock_name, start_date, end_date):
    return web.DataReader(stock_name, 'yahoo', start_date, end_date)


# plot o preço da ação da wege3.sa dos ultimos 12 meses
def plot_stock_price():
    stock_name = 'WEGE3.SA'
    data = get_stock_price(stock_name, datetime.datetime.now() - datetime.timedelta(days=365), datetime.datetime.now())
    data['Close'].plot()
    plt.show()

# plot_stock_price()


# plot the stock price of the wege3.sa since june 2017
def plot_stock_price_since_june_2017():
    stock_name = 'WEGE3.SA'
    data = get_stock_price(stock_name, datetime.datetime(2017, 6, 1), datetime.datetime.now())
    data['Close'].plot()
    plt.show()

# plot_stock_price_since_june_2017()


# salve os preços da ação da wege3.sa desde junho de 2015 num arquivo csv chamado wege3.csv
def save_stock_price_since_june_2017():
    stock_name = 'WEGE3.SA'
    data = get_stock_price(stock_name, datetime.datetime(2015, 6, 1), datetime.datetime.now())
    data.to_csv('wege3.csv')

# save_stock_price_since_june_2017()


# importe o aquivo de preços da ação da wege3.sa
def import_stock_price_since_june_2017():
    data = pd.read_csv('wege3.csv')
    data.plot(x='Date', y='Close')
    plt.show()


# create a candle stick plot of the stock price of the wege3.sa from june 2020
def create_candle_stick_chart():


create_candle_stick_chart()














