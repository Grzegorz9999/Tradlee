
def get_rsi_tesla():
    ticker = pdr.get_data_yahoo("TSLA", datetime(2022, 1, 1))
    delta = ticker['Close'].diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    ema_up = up.ewm(com=13, adjust=False).mean()
    ema_down = down.ewm(com=13, adjust=False).mean()
    rs = ema_up / ema_down
    ticker['RSI'] = 100 - (100 / (1 + rs))
    ticker = ticker.iloc[14:]
    ticker = ticker.iloc[-1:]
    return ticker['RSI']

