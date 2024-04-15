# This Python file uses the following encoding: utf-8
import sys
import json

import stock_data_lib as stlib 

        
stock_input_path="../example/input-stock1.json"

def load_stock_from_json_file(filepath):
    f = open(filepath) 
    data = json.load(f) 
    return data;
    
if __name__ == "__main__":

    # Opening JSON file 
    
    stock_data = load_stock_from_json_file(stock_input_path) 
    
    print(json.dumps(stock_data, indent=4))
    
    stock_data_full=stlib.get_stock_data_full(stock_data);
    
    print(json.dumps(stock_data_full, indent=4))
    

