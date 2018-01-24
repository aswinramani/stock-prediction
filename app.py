import pandas as pd
import matplotlib.pyplot as graph

def plot_data(df):
    axis = df.plot(title="Stock Prices",fontsize=2)
    axis.set_xlabel("Date")
    axis.set_ylabel("Prices")
    graph.show()

def plot_data_daily_returns(df, title="Stock prices", xlabel="Date", ylabel="Prices"):
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    graph.show()

def get_normalized_data(df):
    return df/df.ix[0,:] 

def get_data(symbols, dates):
    df =  pd.DataFrame(index=dates)
    for symbol in symbols:   
        df_symbol = pd.read_csv("data/{}.csv".format(symbol), index_col='Date', parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_symbol = df_symbol.rename(columns={'Adj Close': symbol})
        df = df.join(df_symbol)
    # Step 1a Drop NaN values
    df = df.dropna()
    return df

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
    plot_data(df)
    # Rolling mean
    rm_NFLX = get_rolling_mean(df['NFLX'], window=20)
    # Rolling Standard Deviation
    rstd_NFLX = get_rolling_std(df['NFLX'], window=20)
    # Determine upper and lower bands
    upper_band, lower_band = get_bollinger_bands(rm_NFLX, rstd_NFLX)
    # Plot raw NFLX values, rolling mean and Bollinger Bands
    ax = df['NFLX'].plot(title="Bollinger Bands", label='NFLX')
    rm_NFLX.plot(label='Rolling mean', ax=ax)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    graph.show()

    # Calculate daily returns
    daily_returns = compute_daily_returns(df)
    # Calculate cumulative returns
    cumulative_returns = get_normalized_data(df)
    # print daily_returns
    plot_data_daily_returns(daily_returns, title="Daily returns", ylabel="Daily returns")
    plot_data_daily_returns(cumulative_returns, title="Cumulative returns", ylabel="Cumulative returns")

if __name__ == "__main__":
    init()