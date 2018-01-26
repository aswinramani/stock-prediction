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