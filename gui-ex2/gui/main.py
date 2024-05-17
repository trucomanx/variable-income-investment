# This Python file uses the following encoding: utf-8
import sys
import json

from PySide6.QtWidgets import (QTableWidget,QLabel,QLineEdit, QPushButton, QApplication,
    QHBoxLayout, QDialog)
    
import stock_table_lib as stlib 

class Form(QDialog):

    def __init__(self,stock_data, parent=None):
    
        self.RowItem={};

            
        super(Form, self).__init__(parent)
        
        layout = QHBoxLayout()
        self.table = QTableWidget();
        
        stlib.createTable(self.table,stock_data,stlib.TOTAL_FINANCE_LIST,stlib.FMT_NUM);
        layout.addWidget(self.table);
        
        # Set dialog layout
        self.setLayout(layout)
        
        self.setGeometry(0, 0, 1600, 250)
        

        
        
stock_input_path="../../example/input-stock.json"

def load_stock_from_json_file(filepath):
    f = open(filepath) 
    data = json.load(f) 
    return data;
    
if __name__ == "__main__":

    # Opening JSON file 
    
    stock_data = load_stock_from_json_file(stock_input_path) 
    keysList = list(stock_data.keys())
    
    for key in keysList:
        print(key,stock_data[key]["qty"],stock_data[key]["averagePrice"]);
    

    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form(stock_data)
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
