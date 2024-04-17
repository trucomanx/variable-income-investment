import yfinance as yf

################################################################################
################################################################################

## Gain functions
import functions_gain as funcs_gain

## Information functions
import functions_info as funcs_info

## History functions
import functions_hist as funcs_hist

## Fundamental functions
import functions_fundamental_valuation as funcs_fval

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
        funcs_gain.add_data_initialAmount(stock_data_full,stock_name,stock_obj);
        funcs_gain.add_data_finalAmount(stock_data_full,stock_name,stock_obj);
        funcs_gain.add_data_gainAmount(stock_data_full,stock_name,stock_obj);
        funcs_gain.add_data_gainAmountPercentage(stock_data_full,stock_name,stock_obj);
        
        ## Information functions
        funcs_info.add_data_currency(stock_data_full,stock_name,stock_obj);
        funcs_info.add_data_currentPrice(stock_data_full,stock_name,stock_obj);
        funcs_info.add_data_longName(stock_data_full,stock_name,stock_obj);
        funcs_info.add_data_sectorKey(stock_data_full,stock_name,stock_obj);
        funcs_info.add_data_industryKey(stock_data_full,stock_name,stock_obj);
        
        ## History functions
        funcs_hist.add_data_shortDiffPercent(stock_data_full,stock_name,stock_obj);
        funcs_hist.add_data_shortDataPrices(stock_data_full,stock_name,stock_obj);
        funcs_hist.add_data_longDiffPercent(stock_data_full,stock_name,stock_obj);
        funcs_hist.add_data_longDataPrices(stock_data_full,stock_name,stock_obj);
        
        ## Fundamental Valuation Indicators:
        funcs_fval.add_data_trailingAnnualDividendYield(stock_data_full,stock_name,stock_obj);
        funcs_fval.add_data_bookValue(stock_data_full,stock_name,stock_obj);
        funcs_fval.add_data_priceToBook(stock_data_full,stock_name,stock_obj);
        funcs_fval.add_data_enterpriseToRevenue(stock_data_full,stock_name,stock_obj);
        funcs_fval.add_data_trailingPE(stock_data_full,stock_name,stock_obj);
        funcs_fval.add_data_linearPE(stock_data_full,stock_name,stock_obj);
        
        ## Fundamental Profitability Indicators:
        funcs_fval.add_data_returnOnEquity(stock_data_full,stock_name,stock_obj);
        funcs_fval.add_data_returnOnAssets(stock_data_full,stock_name,stock_obj);
        funcs_fval.add_data_trailingEps(stock_data_full,stock_name,stock_obj);
        funcs_fval.add_data_basicEps(stock_data_full,stock_name,stock_obj);
        funcs_fval.add_data_payoutRatio(stock_data_full,stock_name,stock_obj);
        
        ## Fundamental fair price Indicators:
        funcs_fval.add_data_profitMargins(stock_data_full,stock_name,stock_obj);
        funcs_fval.add_data_trailingGrahamValue(stock_data_full,stock_name,stock_obj);
        funcs_fval.add_data_forwardGrahamValue(stock_data_full,stock_name,stock_obj);
        funcs_fval.add_data_trailingBazinValue(stock_data_full,stock_name,stock_obj);
        funcs_fval.add_data_forwardBazinValue(stock_data_full,stock_name,stock_obj);
        
    return stock_data_full
