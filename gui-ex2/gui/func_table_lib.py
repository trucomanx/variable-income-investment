from PyQt5.QtWidgets import QTableWidgetItem
import json 


import copy

def get_full_default_data(  default_data,
                            default_labels):
    default_labels_full = copy.deepcopy(default_labels);
    for key in default_labels_full.keys():
        default_labels_full[key]["data"]=copy.deepcopy(default_data[default_labels[key]["type"]]);
        
        if "data" in default_labels[key]:
            for label in default_labels[key]["data"]:
                default_labels_full[key]["data"][label] = copy.deepcopy(default_labels[key]["data"][label]);
    return default_labels_full;

def remakeTable(tableWidget,
                stock_data,
                index_data,
                default_data,
                default_labels):
    
    
    
    ############################################################################
    ## Creating default_labels_full and title_list
    
    default_labels_full = get_full_default_data(default_data, default_labels);
    
    title_list=[];
    for tipo in index_data.keys():
        for index in index_data[tipo].keys():
            for key in index_data[tipo][index].keys():
                default_labels_full[index]["data"][key]=copy.deepcopy(index_data[tipo][index][key]);
            if default_labels_full[index]["data"]["title"]==None:
                title_list.append(index);
            else:
                title_list.append(default_labels_full[index]["data"]["title"]);
    
    #print(json.dumps(default_labels_full, indent=4));
    
    ############################################################################
    
    tableWidget.clear();
    num_rows=len(stock_data.keys());
    num_cols=len(title_list);

    tableWidget.setRowCount(num_rows) ; 
    tableWidget.setColumnCount(num_cols);
    
    tableWidget.setHorizontalHeaderLabels(title_list);
    tableWidget.setVerticalHeaderLabels(list(stock_data.keys()));
    

    
    for row in range(num_rows):
        for col in range(num_cols):
            item = QTableWidgetItem(f"({row+1},{col+1})")
            tableWidget.setItem(row, col, item)
    
