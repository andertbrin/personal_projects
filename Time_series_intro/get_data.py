import yfinance as yf
import datetime


def get_stock_close_price(ticker):
    today = str(datetime.datetime.today())[0:10]
    df = yf.download(ticker, start='2010-01-01', end=today)

    # removing all the columns except the 'Close' prices
    df = df[['Close']]

    df = df.fillna(method='ffill')  # forward filling
    df = df.fillna(method='bfill')  # backward filling
    return df
