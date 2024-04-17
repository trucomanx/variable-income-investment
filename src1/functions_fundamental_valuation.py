import math 
import datetime
import numpy as np


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
    

## Fundamental Profitability Indicators:

def add_data_returnOnEquity(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['returnOnEquity']=None;
    if 'returnOnEquity' in stock_obj.info:
        stock_data[stock_name]['returnOnEquity']=100.0*stock_obj.info['returnOnEquity'];

def add_data_returnOnAssets(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['returnOnAssets']=None;
    if 'returnOnAssets' in stock_obj.info:
        stock_data[stock_name]['returnOnAssets']=100.0*stock_obj.info['returnOnAssets'];

def add_data_trailingEps(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['trailingEps']=None;
    if 'trailingEps' in stock_obj.info:
        stock_data[stock_name]['trailingEps']=stock_obj.info['trailingEps'];

def add_data_basicEps(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['basicEps']={'time':None,'eps':None,'rate':None};
    if 'Basic EPS' in stock_obj.financials.index:
        today = datetime.date.today()
        year = today.year
        
        df=stock_obj.financials.loc['Basic EPS'];
        eps=list(df);
        time=[ t.year for t in df.index];
        
        eps.reverse();
        time.reverse();
        
        ## Si el retorno es negativo entonces el lucro nan es cero
        for i in range(len(eps)):
            if np.isnan(eps[i]):
                if time[i]==(year-1):
                    eps[i]=stock_obj.info['trailingEps'];
                elif stock_obj.info['returnOnEquity']<=0:
                    eps[i]=0.0;
        
        ## Drop nan #####
        indices_nan = [i for i, x in enumerate(eps) if np.isnan(x)]
        eps  = [x for i, x in enumerate(eps)  if i not in indices_nan];
        time = [x for i, x in enumerate(time) if i not in indices_nan];
        #################
        
        x = np.array(time);
        y = np.array(eps);
        
        m, b = np.polyfit(x, y, 1)
        
        S=0;
        for i in range(len(eps)):
            S=S+math.pow(eps[i]-m*time[i]-b,2);
        S=math.sqrt(S/len(eps));
            
        stock_data[stock_name]['basicEps']={
            'time':time,
            'eps':eps,
            'mseGrowthPerYear':m,
            'mseEps0':m*(year-1)+b, #EPS of last year
            'mseEps0Rmse':S # rmse of linear fitting
        };
        # EPScurrent=m*(year-YearCurrent+1)+mseEps0

def add_data_payoutRatio(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['payoutRatio']=None;
    if 'payoutRatio' in stock_obj.info:
        stock_data[stock_name]['payoutRatio']=100.0*stock_obj.info['payoutRatio'];

def add_data_profitMargins(stock_data,stock_name,stock_obj):#Margem liquida # net profit margin
    stock_data[stock_name]['profitMargins']=None;
    if 'profitMargins' in stock_obj.info:
        stock_data[stock_name]['profitMargins']=100.0*stock_obj.info['profitMargins'];


## Fundamental fair price Indicators:

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

