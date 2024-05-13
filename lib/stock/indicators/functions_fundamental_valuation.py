import math 

## Fundamental Valuation Indicators:

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

def add_data_enterpriseToRevenue(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['enterpriseToRevenue']=None;
    if 'enterpriseToRevenue' in stock_obj.info:
        stock_data[stock_name]['enterpriseToRevenue']=stock_obj.info['enterpriseToRevenue'];

def add_data_trailingPE(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['trailingPE']=None;
    if 'trailingPE' in stock_obj.info:
        stock_data[stock_name]['trailingPE']=stock_obj.info['trailingPE'];

def add_data_linearPE(stock_data,stock_name,stock_obj):
    PL=None;
    if 'trailingPE' in stock_obj.info:
        PL=stock_obj.info['trailingPE'];
    
    stock_data[stock_name]['linearPE']={'pct':None,'time':None};
    
    if PL!=None:
        pct=list(range(16))
        time=[0]*len(pct)
        
        n=0;
        for p in pct:
            if p==0:
                time[n]=PL;
            else:
                time[n]=-(100.0/p+0.5)+math.sqrt(math.pow(100.0/p+0.5,2) + (200.0/p)*PL);
            n=n+1;
        
        stock_data[stock_name]['linearPE']={'pct':pct,'time':time};
    

################################################################################
################################################################################
################################################################################

def add_fundamental_valuation_indicators(stock_data,stock_name,stock_obj):
        add_data_trailingAnnualDividendYield(stock_data,stock_name,stock_obj);
        add_data_bookValue(stock_data,stock_name,stock_obj);
        add_data_priceToBook(stock_data,stock_name,stock_obj);
        add_data_enterpriseToRevenue(stock_data,stock_name,stock_obj);
        add_data_trailingPE(stock_data,stock_name,stock_obj);
        add_data_linearPE(stock_data,stock_name,stock_obj);


