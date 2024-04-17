# This Python file uses the following encoding: utf-8

import json

import stock.indicators_lib as stlib 
import stock.load_dict      as lsd

if __name__ == "__main__":
    
    stock_input_path="../example/input-stock1.json"
    
    # Opening JSON file
    stock_data = lsd.load_stock_dict_from_json_file(stock_input_path);
    
    print(json.dumps(stock_data, indent=4))
    
    stock_data_full=stlib.get_stock_data_full(stock_data);
    
    print(json.dumps(stock_data_full, indent=4))
    

