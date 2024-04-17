
## Fundamental Indebtedness Indicators:

def add_data_debtToEquity(stock_data,stock_name,stock_obj):
    # Selecione a dívida total e o patrimônio líquido
    divida_total = stock_obj.balance_sheet.loc['Total Debt'].iloc[0];
    patrimonio_liquido = stock_obj.balance_sheet.loc['Stockholders Equity'].iloc[0];
    
    # Calcule a relação dívida/patrimônio líquido
    debt_to_equity_ratio = divida_total / patrimonio_liquido;
    
    stock_data[stock_name]['debtToEquity']=debt_to_equity_ratio*100;

################################################################################
################################################################################
################################################################################

def add_fundamental_deb_indicators(stock_data,stock_name,stock_obj):
    add_data_debtToEquity(stock_data,stock_name,stock_obj);
