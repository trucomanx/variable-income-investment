import json

def load_stock_dict_from_json_file(filepath):
    f = open(filepath) 
    data = json.load(f) 
    return data;

