import math 

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

################################################################################
################################################################################
################################################################################

def add_fundamental_fair_price_indicators(stock_data,stock_name,stock_obj,anual_inflation=0.04):
    add_data_trailingGrahamValue(stock_data,stock_name,stock_obj);
    add_data_forwardGrahamValue(stock_data,stock_name,stock_obj);
    add_data_trailingBazinValue(stock_data,stock_name,stock_obj,anual_inflation);
    add_data_forwardBazinValue(stock_data,stock_name,stock_obj,anual_inflation);
