import yfinance as yf

################################################################################
################################################################################

## Gain functions
import stock.indicators.functions_gain as funcs_gain

## Information functions
import stock.indicators.functions_info as funcs_info

## History functions
import stock.indicators.functions_hist as funcs_hist

## Fundamental valuation functions
import stock.indicators.functions_fundamental_valuation as funcs_fval

## Fundamental profit functions
import stock.indicators.functions_fundamental_profit as funcs_fpro

## Fundamental deb functions
import stock.indicators.functions_fundamental_deb as funcs_fdeb

## Fundamental fair price functions
import stock.indicators.functions_fundamental_price as funcs_fpri

################################################################################
################################################################################

def get_stock_data_full(stock_data):
    stock_data_full=stock_data.copy();
    
    for stock_name in stock_data_full:
        stock_obj=yf.Ticker(stock_name);
        
        #print(stock_obj.actions,'\n');
        #print(stock_obj.balance_sheet,'\n');
        #print(stock_obj.financials,'\n');
        #print(stock_obj.cashflow,'\n');
        
        ## Gain functions
        funcs_gain.add_gain_indicators(stock_data_full,stock_name,stock_obj);
        
        ## Information functions
        funcs_info.add_information_indicators(stock_data_full,stock_name,stock_obj);
        
        ## History functions
        funcs_hist.add_history_indicators(stock_data_full,stock_name,stock_obj);
        
        ## Fundamental Valuation Indicators:
        funcs_fval.add_fundamental_valuation_indicators(stock_data_full,stock_name,stock_obj);
        
        ## Fundamental Profitability Indicators:
        funcs_fpro.add_fundamental_profit_indicators(stock_data_full,stock_name,stock_obj);
        
        ## Fundamental Indebtedness Indicators:
        funcs_fdeb.add_fundamental_deb_indicators(stock_data_full,stock_name,stock_obj);
        
        ## Fundamental fair price Indicators:
        funcs_fpri.add_fundamental_fair_price_indicators(stock_data_full,stock_name,stock_obj);
        
    return stock_data_full
