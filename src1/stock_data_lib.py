import yfinance as yf
import math 

#####################

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

## History functions

def add_data_shortDiffPercent(stock_data,stock_name,stock_obj,days_plot=15):
    Data = yf.Ticker(stock_name).history(period=str(days_plot)+"d")
    
    diff_percent=100.0*(Data['Close'].iloc[-1]/Data['Close'].iloc[0]-1.0);
    
    stock_data[stock_name]['shortDiffPercent']=diff_percent;

def add_data_shortDataPrices(stock_data,stock_name,stock_obj,days_plot=15):
    DATA=yf.download(stock_name, period=str(days_plot)+'d',progress=False)
    price=list(DATA['Adj Close']);    
    time=list(range(len(price)));
    
    stock_data[stock_name]['shortDataPrices']={'time': time,'price': price};

def add_data_longDiffPercent(stock_data,stock_name,stock_obj,days_plot=180):
    Data = yf.Ticker(stock_name).history(period=str(days_plot)+"d")
    
    diff_percent=100.0*(Data['Close'].iloc[-1]/Data['Close'].iloc[0]-1.0);
    
    stock_data[stock_name]['longDiffPercent']=diff_percent;

def add_data_longDataPrices(stock_data,stock_name,stock_obj,days_plot=180):
    DATA=yf.download(stock_name, period=str(days_plot)+'d',progress=False)
    price=list(DATA['Adj Close']);    
    time=list(range(len(price)));
    
    stock_data[stock_name]['longDataPrices']={'time': time,'price': price};

## Fundamental functions

def add_data_trailingAnnualDividendYield(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['trailingAnnualDividendYield']=None;
    if 'trailingAnnualDividendYield' in stock_obj.info:
        stock_data[stock_name]['trailingAnnualDividendYield']=stock_obj.info['trailingAnnualDividendYield'];

def add_data_bookValue(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['bookValue']=None;
    if 'bookValue' in stock_obj.info:
        stock_data[stock_name]['bookValue']=stock_obj.info['bookValue'];

def add_data_priceToBook(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['priceToBook']=None;
    if 'priceToBook' in stock_obj.info:
        stock_data[stock_name]['priceToBook']=stock_obj.info['priceToBook'];

def add_data_returnOnEquity(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['returnOnEquity']=None;
    if 'returnOnEquity' in stock_obj.info:
        stock_data[stock_name]['returnOnEquity']=100.0*stock_obj.info['returnOnEquity'];

def add_data_returnOnAssets(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['returnOnAssets']=None;
    if 'returnOnAssets' in stock_obj.info:
        stock_data[stock_name]['returnOnAssets']=100.0*stock_obj.info['returnOnAssets'];

def add_data_enterpriseToRevenue(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['enterpriseToRevenue']=None;
    if 'enterpriseToRevenue' in stock_obj.info:
        stock_data[stock_name]['enterpriseToRevenue']=stock_obj.info['enterpriseToRevenue'];

def add_data_trailingPE(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['trailingPE']=None;
    if 'trailingPE' in stock_obj.info:
        stock_data[stock_name]['trailingPE']=stock_obj.info['trailingPE'];

def add_data_trailingEps(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['trailingEps']=None;
    if 'trailingEps' in stock_obj.info:
        stock_data[stock_name]['trailingEps']=stock_obj.info['trailingEps'];

def add_data_payoutRatio(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['payoutRatio']=None;
    if 'payoutRatio' in stock_obj.info:
        stock_data[stock_name]['payoutRatio']=100.0*stock_obj.info['payoutRatio'];

def add_data_profitMargins(stock_data,stock_name,stock_obj):#Margem liquida
    stock_data[stock_name]['profitMargins']=None;
    if 'profitMargins' in stock_obj.info:
        stock_data[stock_name]['profitMargins']=100.0*stock_obj.info['profitMargins'];

def add_data_trailingGrahamValue(stock_data,stock_name,stock_obj):
    vpa=None;
    eps=None;
    if 'bookValue' in stock_obj.info:
        vpa=stock_obj.info['bookValue'];
    if 'trailingEps' in stock_obj.info:
        eps=stock_obj.info['trailingEps'];
    
    if vpa!=None and vpa>=0 and eps!=None and eps>=0:
        stock_data[stock_name]['trailingGrahamValue']=math.sqrt(22.5*vpa*eps);
    else:
        stock_data[stock_name]['trailingGrahamValue']=None;

def add_data_forwardGrahamValue(stock_data,stock_name,stock_obj):
    vpa=None;
    eps=None;
    if 'bookValue' in stock_obj.info:
        vpa=stock_obj.info['bookValue'];
    if 'forwardEps' in stock_obj.info:
        eps=stock_obj.info['forwardEps'];
    
    if vpa!=None and vpa>=0 and eps!=None and eps>=0:
        stock_data[stock_name]['forwardGrahamValue']=math.sqrt(22.5*vpa*eps);
    else:
        stock_data[stock_name]['forwardGrahamValue']=None;

def add_data_trailingBazinValue(stock_data,stock_name,stock_obj,anual_inflation=0.04):
    eps=None;
    if 'trailingEps' in stock_obj.info:
        eps=stock_obj.info['trailingEps'];
    
    if eps!=None and eps>=0:
        stock_data[stock_name]['trailingBazinValue']=eps/(anual_inflation+0.06);
    else:
        stock_data[stock_name]['trailingBazinValue']=None;

def add_data_forwardBazinValue(stock_data,stock_name,stock_obj,anual_inflation=0.04):
    eps=None;
    if 'forwardEps' in stock_obj.info:
        eps=stock_obj.info['forwardEps'];
    
    if eps!=None and eps>=0:
        stock_data[stock_name]['forwardBazinValue']=eps/(anual_inflation+0.06);
    else:
        stock_data[stock_name]['forwardBazinValue']=None;

#####################
def get_stock_data_full(stock_data):
    stock_data_full=stock_data.copy();
    
    for stock_name in stock_data_full:
        stock_obj=yf.Ticker(stock_name);
        
        #history = stock_obj.history(period="max", actions=True)
        #print(history.columns,'\n',history,'\n');
        
        '''
        for label in stock_obj.balance_sheet.index:
            print(label)
        print('\n')
        '''
        
        print(stock_obj.dividends,'\n')
        print(list(stock_obj.dividends),'\n')
        
        '''
        for label in stock_obj.cashflow.index:
            print(label)
        print('\n')
        '''
        
        ## Gain functions
        add_data_initialAmount(stock_data_full,stock_name,stock_obj);
        add_data_finalAmount(stock_data_full,stock_name,stock_obj);
        add_data_gainAmount(stock_data_full,stock_name,stock_obj);
        add_data_gainAmountPercentage(stock_data_full,stock_name,stock_obj);
        
        ## Information functions
        add_data_currency(stock_data_full,stock_name,stock_obj);
        add_data_currentPrice(stock_data_full,stock_name,stock_obj);
        add_data_longName(stock_data_full,stock_name,stock_obj);
        add_data_sectorKey(stock_data_full,stock_name,stock_obj);
        add_data_industryKey(stock_data_full,stock_name,stock_obj);
        
        ## History functions
        add_data_shortDiffPercent(stock_data_full,stock_name,stock_obj);
        add_data_shortDataPrices(stock_data_full,stock_name,stock_obj);
        add_data_longDiffPercent(stock_data_full,stock_name,stock_obj);
        add_data_longDataPrices(stock_data_full,stock_name,stock_obj);
        
        ## Fundamental functions
        add_data_trailingAnnualDividendYield(stock_data_full,stock_name,stock_obj);
        add_data_bookValue(stock_data_full,stock_name,stock_obj);
        add_data_priceToBook(stock_data_full,stock_name,stock_obj);
        add_data_returnOnEquity(stock_data_full,stock_name,stock_obj);
        add_data_returnOnAssets(stock_data_full,stock_name,stock_obj);
        add_data_enterpriseToRevenue(stock_data_full,stock_name,stock_obj);
        add_data_trailingPE(stock_data_full,stock_name,stock_obj);
        add_data_trailingEps(stock_data_full,stock_name,stock_obj);
        add_data_payoutRatio(stock_data_full,stock_name,stock_obj);
        add_data_profitMargins(stock_data_full,stock_name,stock_obj);
        add_data_trailingGrahamValue(stock_data_full,stock_name,stock_obj);
        add_data_forwardGrahamValue(stock_data_full,stock_name,stock_obj);
        add_data_trailingBazinValue(stock_data_full,stock_name,stock_obj);
        add_data_forwardBazinValue(stock_data_full,stock_name,stock_obj);
        
    return stock_data_full
