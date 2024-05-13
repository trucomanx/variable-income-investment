

## Information functions

def add_data_currency(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['currency']=stock_obj.info['currency'];

def add_data_currentPrice(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['currentPrice']=stock_obj.info['currentPrice'];

def add_data_longName(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['longName']=stock_obj.info['longName'];

def add_data_industryKey(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['industryKey']=stock_obj.info['industryKey'];

def add_data_sectorKey(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['sectorKey']=stock_obj.info['sectorKey'];

################################################################################
################################################################################
################################################################################

def add_information_indicators(stock_data,stock_name,stock_obj):
    add_data_currency(stock_data,stock_name,stock_obj);
    add_data_currentPrice(stock_data,stock_name,stock_obj);
    add_data_longName(stock_data,stock_name,stock_obj);
    add_data_sectorKey(stock_data,stock_name,stock_obj);
    add_data_industryKey(stock_data,stock_name,stock_obj);


