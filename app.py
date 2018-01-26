import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
from util import get_data, plot_data, plot_histogram

# debug function
def print_df(df, head=True):
    if head:
        print df.head()    
    else:
        print df.tail()

def get_normalized_data(df):
    return df/df.ix[0,:] 

def compute_daily_returns(df):
    daily_returns = df.copy()
    # daily_returns[1:] = df[1:]/df[:-1].values - 1
    daily_returns = (df / df.shift(1)) - 1 
    # Replace NaN values with 0 for 0th row
    daily_returns.ix[0, :] = 0 
    return daily_returns

def get_portfolio_stats(df):
    investment = 100000
    allocs = [0.2, 0.2, 0.2, 0.2, 0.2]
    # allocs = [100, 10, 10, 100, 10]
    # Step 1 Compute Cumulative Return 
    cumulative_returns = get_normalized_data(df)
    # Step 2 Multiply normalized data with allocations
    alloc_val = cumulative_returns * allocs
    # Step 3 Multiply alloc_val with initial investment
    invst_val = alloc_val * investment
    # Step 4 Compute the total portfolio value for each day 
    port_val = invst_val.sum(axis=1)
    pstat_daily_rets = compute_daily_returns(df)
    pstat_daily_rets = pstat_daily_rets[1:]
    avg_daily_rets = pstat_daily_rets.mean()
    std_daily_rets = pstat_daily_rets.std()
    # print_df(pstat_daily_rets[1:])
    return port_val, pstat_daily_rets, cumulative_returns, avg_daily_rets, std_daily_rets

def init():
    dates = pd.date_range('2016-01-07', '2017-01-05')
    symbols = ["AAPL", "MSFT", "AMZN", "FB", "BRK-B"]
    # Step 1 initialize dataframe and combine all input data into one
    df = get_data(symbols, dates)
    # plot_data(df)
    # Calculate daily returns
    # daily_returns = compute_daily_returns(df)
    # # plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")
    # plot_histogram(daily_returns, symbols)

    # # Calculate cumulative returns
    # cumulative_returns = get_normalized_data(df)
    # # print daily_returns

    # Compute Portfolio Value
    port_val, pstat_daily_rets, cumulative_returns, avg_daily_rets, std_daily_rets = get_portfolio_stats(df)
    # ax = df['NFLX'].plot(title="Bollinger Bands", label='NFLX')
    # rm_NFLX.plot(label='Rolling mean', ax=ax)
    ax = port_val.plot(title="Portfolio Statistics", label='Portfolio Val')
    # port_val.plot(label='Current Val', ax=ax)

    # # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()
    
    # plot_data_daily_returns(cumulative_returns, title="Cumulative returns", ylabel="Cumulative returns")

if __name__ == "__main__":
    init()