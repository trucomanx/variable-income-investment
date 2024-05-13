import datetime
import numpy as np
import math 


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
        
        ## Fit
        x = np.array(time);
        y = np.array(eps);
        
        m, b = np.polyfit(x, y, 1);
        
        ## rmse
        S=0;
        for i in range(len(eps)):
            S=S+math.pow(eps[i]-m*time[i]-b,2);
        S=math.sqrt(S/len(eps));
         
        ## end
        stock_data[stock_name]['basicEps']={
            'time':time,
            'eps':eps,
            'mseGrowthPerYear':m,
            'mseEps0':m*(year-1)+b, #EPS of last year
            'mseEps0Rmse':S # rmse of linear fitting
        };
        # EPScurrent=m*(year-YearCurrent+1)+mseEps0

def add_data_histNetIncome(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['histNetIncome']={'time':None,'hni':None,'rate':None};
    
    if 'Net Income' in stock_obj.financials.index:
        today = datetime.date.today();
        year = today.year;
        
        df=stock_obj.financials.loc['Net Income'];
        hni=list(df);
        hni =[x/1000000.0 for x in hni];
        time=[ t.year     for t in df.index];
        
        hni.reverse();
        time.reverse();
        
        ## Fit
        x = np.array(time);
        y = np.array(hni);
        w = np.linspace(1,1*len(hni),len(hni)); w=w/np.sum(w);
        
        m, b = np.polyfit(x, y, 1,w=w);
        
        ## rmse
        S=0;
        for i in range(len(hni)):
            S=S+math.pow(hni[i]-m*time[i]-b,2);
        S=math.sqrt(S/len(hni));
        
        ## end
        mseHni0=m*(year-1)+b;
        stock_data[stock_name]['histNetIncome']={
            'time':time,
            'hni':hni, # 10^6
            'mseGrowthPerYear':m, # 10^6
            'mseHni0':mseHni0, # 10^6 # predicted net income of last year
            'mseHni0Rmse':S, # 10^6 # rmse of linear fitting
            'mseGrowthPercent':m*100/np.abs(mseHni0),
            'mseErrorPercent':S*100/np.abs(mseHni0)
        };
        
def add_data_payoutRatio(stock_data,stock_name,stock_obj):
    stock_data[stock_name]['payoutRatio']=None;
    if 'payoutRatio' in stock_obj.info:
        stock_data[stock_name]['payoutRatio']=100.0*stock_obj.info['payoutRatio'];

def add_data_profitMargins(stock_data,stock_name,stock_obj):#Margem liquida # net profit margin
    stock_data[stock_name]['profitMargins']=None;
    if 'profitMargins' in stock_obj.info:
        stock_data[stock_name]['profitMargins']=100.0*stock_obj.info['profitMargins'];

################################################################################
################################################################################
################################################################################

def add_fundamental_profit_indicators(stock_data,stock_name,stock_obj):
    add_data_returnOnEquity(stock_data,stock_name,stock_obj);
    add_data_returnOnAssets(stock_data,stock_name,stock_obj);
    add_data_trailingEps(stock_data,stock_name,stock_obj);
    add_data_basicEps(stock_data,stock_name,stock_obj);
    add_data_histNetIncome(stock_data,stock_name,stock_obj);
    add_data_payoutRatio(stock_data,stock_name,stock_obj);
    add_data_profitMargins(stock_data,stock_name,stock_obj);

