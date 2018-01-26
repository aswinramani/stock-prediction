import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
from util import get_data, plot_data, plot_histogram

def get_normalized_data(df):
    return df/df.ix[0,:] 

def get_rolling_mean(values, window):
    # return pd.rolling_mean(values, window=window) --> Deprecated Code
    return values.rolling(window=window, center=False).mean()

def get_rolling_std(values, window):
    # return pd.rolling_std(values, window=window) --> Deprecated Code
    return values.rolling(window=window, center=False).std()

def get_bollinger_bands(rm, rstd):
    upper_band = rm + (rstd*2)
    lower_band = rm - (rstd*2)
    # return np.round(rm,3), np.round(upband,3), np.round(dnband,3)
    return upper_band, lower_band

def compute_daily_returns(df):
    daily_returns = df.copy()
    # daily_returns[1:] = df[1:]/df[:-1].values - 1
    daily_returns = (df / df.shift(1)) - 1 
    # Replace NaN values with 0 for 0th row
    daily_returns.ix[0, :] = 0 
    return daily_returns

def init():
    dates = pd.date_range('2016-01-07', '2017-01-05')
    symbols = ["AAPL", "FB", "GOOG", "NFLX", "TSLA"]
    # Step 1 initialize dataframe and combine all input data into one
    df = get_data(symbols, dates)
    # plot_data(df)
    # # Rolling mean
    # rm_NFLX = get_rolling_mean(df['NFLX'], window=20)
    # # Rolling Standard Deviation
    # rstd_NFLX = get_rolling_std(df['NFLX'], window=20)
    # # Determine upper and lower bands
    # upper_band, lower_band = get_bollinger_bands(rm_NFLX, rstd_NFLX)
    # # Plot raw NFLX values, rolling mean and Bollinger Bands
    # ax = df['NFLX'].plot(title="Bollinger Bands", label='NFLX')
    # rm_NFLX.plot(label='Rolling mean', ax=ax)
    # upper_band.plot(label='upper band', ax=ax)
    # lower_band.plot(label='lower band', ax=ax)

    # # Add axis labels and legend
    # ax.set_xlabel("Date")
    # ax.set_ylabel("Price")
    # ax.legend(loc='upper left')
    # plt.show()

    # Calculate daily returns
    daily_returns = compute_daily_returns(df)
    # plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")
    plot_histogram(daily_returns, symbols)

    # # Calculate cumulative returns
    # cumulative_returns = get_normalized_data(df)
    # # print daily_returns
    
    # plot_data_daily_returns(cumulative_returns, title="Cumulative returns", ylabel="Cumulative returns")

if __name__ == "__main__":
    init()