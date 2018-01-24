import pandas as pd
import matplotlib.pyplot as graph

def plot_data(df):
    axis = df.plot(title="Stock Prices",fontsize=2)
    axis.set_xlabel("Date")
    axis.set_ylabel("Prices")
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

def init():
    dates = pd.date_range('2016-01-01', '2018-01-15')
    symbols = ["AAPL", "FB", "GOOG", "NFLX", "TSLA"]
    # Step 1 initialize dataframe and combine all input data into one
    df = get_data(symbols, dates)
    # Step 2 Normalize data
    df = get_normalized_data(df)
    # Step 3 Plot the Normalized data
    plot_data(df)


if __name__ == "__main__":
    init()