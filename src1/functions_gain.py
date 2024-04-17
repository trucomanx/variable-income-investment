

## Gain functions

def add_data_initialAmount(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['initialAmount']=stock_data[stock_name]['qty']*stock_data[stock_name]['averagePrice'];

def add_data_finalAmount(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['finalAmount']=stock_data[stock_name]['qty']*stock_obj.info['currentPrice'];

def add_data_gainAmount(stock_data,stock_name,stock_obj):
    finalAmount   = stock_data[stock_name]['qty']*stock_obj.info['currentPrice'];
    initialAmount = stock_data[stock_name]['qty']*stock_data[stock_name]['averagePrice'];
    stock_data[stock_name]['gainAmount']=finalAmount-initialAmount;

def add_data_gainAmountPercentage(stock_data,stock_name,stock_obj):
    finalAmount   = stock_data[stock_name]['qty']*stock_obj.info['currentPrice'];
    initialAmount = stock_data[stock_name]['qty']*stock_data[stock_name]['averagePrice'];
    stock_data[stock_name]['gainAmountPercentage']=100.0*(finalAmount-initialAmount)/initialAmount;
