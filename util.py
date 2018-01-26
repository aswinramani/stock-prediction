import pandas as pd
import matplotlib.pyplot as plt

def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Prices"):
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()

def plot_histogram(df, symbols):
    for symbol in symbols:
        df[symbol].hist(bins=20, label=symbol)
    plt.legend(loc='upper right')
    # Calculating mean and std dev in order to visulaize them.
    # mean = df['TSLA'].mean()
    # print "mean = ", mean
    # std = df['TSLA'].std()
    # print "std = ", std
    # print "kurtosis =", df.kurtosis()
    print "correlation cofficient"
    print df.corr(method='pearson')
    # plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
    # plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    # plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    # Histogram for Daily Returns
    plt.show()

def get_data(symbols, dates):
    df =  pd.DataFrame(index=dates)
    for symbol in symbols:   
        df_symbol = pd.read_csv("data/{}.csv".format(symbol), index_col='Date', parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_symbol = df_symbol.rename(columns={'Adj Close': symbol})
        df = df.join(df_symbol)
    # Step 1a Drop NaN values
    df = df.dropna()
    return df
