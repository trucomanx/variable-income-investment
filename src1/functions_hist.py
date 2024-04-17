import yfinance as yf
## History functions

def add_data_shortDiffPercent(stock_data,stock_name,stock_obj,days_plot=15):
    Data = stock_obj.history(period=str(days_plot)+"d")
    
    diff_percent=100.0*(Data['Close'].iloc[-1]/Data['Close'].iloc[0]-1.0);
    
    stock_data[stock_name]['shortDiffPercent']=diff_percent;

def add_data_shortDataPrices(stock_data,stock_name,stock_obj,days_plot=15):
    DATA=yf.download(stock_name, period=str(days_plot)+'d',progress=False)
    price=list(DATA['Adj Close']);    
    time=list(range(len(price)));
    
    stock_data[stock_name]['shortDataPrices']={'time': time,'price': price};

def add_data_longDiffPercent(stock_data,stock_name,stock_obj,days_plot=180):
    Data = stock_obj.history(period=str(days_plot)+"d")
    
    diff_percent=100.0*(Data['Close'].iloc[-1]/Data['Close'].iloc[0]-1.0);
    
    stock_data[stock_name]['longDiffPercent']=diff_percent;

def add_data_longDataPrices(stock_data,stock_name,stock_obj,days_plot=180):
    DATA=yf.download(stock_name, period=str(days_plot)+'d',progress=False)
    price=list(DATA['Adj Close']);    
    time=list(range(len(price)));
    
    stock_data[stock_name]['longDataPrices']={'time': time,'price': price};

