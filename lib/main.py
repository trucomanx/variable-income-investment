# This Python file uses the following encoding: utf-8

import json
import os

import stock.indicators_lib as stlib 
import stock.load_dict      as lsd

OUTPUT='output';

os.makedirs(OUTPUT,exist_ok=True);

if __name__ == "__main__":
    
    stock_input_path="../example/input-stock.json"
    
    # Opening JSON file
    stock_data = lsd.load_stock_dict_from_json_file(stock_input_path);
    
    print(json.dumps(stock_data, indent=4))
    
    stock_data_full=stlib.get_stock_data_full(stock_data);
    
    with open(os.path.join(OUTPUT,'data.json'), 'w') as f:
        json.dump(stock_data_full,f, indent=4)

