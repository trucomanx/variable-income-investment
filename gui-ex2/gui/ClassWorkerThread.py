import sys
import os
sys.path.append('../../lib');
import stock.indicators_lib as stlib 
import func_table_lib as tablib

################################################################################
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QTableWidget

import json

class WorkerThread(QThread):
    update_progress = pyqtSignal(int)

    def __init__(self,stock_data,index_data,table):
        super().__init__()
        self.stock_data=stock_data;
        self.index_data=index_data;
        self.table=table;

        script_path = os.path.dirname(os.path.abspath(__file__))
        default_data_file   = os.path.join(script_path,'conf','default-data.json');
        default_labels_file = os.path.join(script_path,'conf','default-labels.json');
        
        with open(default_data_file, 'r') as File:
            self.default_data = json.load(File);
        
        with open(default_labels_file, 'r') as File:
            self.default_labels = json.load(File);
        
    def run(self):
        stock_data_full=stlib.get_stock_data_full(  self.stock_data,
                                                    emit=self.update_progress.emit);
        self.msleep(20);
        self.update_progress.emit(0);
        
        tablib.remakeTable( self.table,
                            stock_data_full,
                            self.index_data,
                            self.default_data,
                            self.default_labels);
