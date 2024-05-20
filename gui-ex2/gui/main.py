import sys
import os
import json

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidget

from PyQt5.QtWidgets import QWidget

import ClassWorkerThread as cwt
        
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Progress Bar Demo")
        layout = QVBoxLayout()
        
        gridLayout = QGridLayout();
        self.btnOpenStockList=QPushButton("Open stock list");
        self.btnOpenStockList.clicked.connect(self.select_stock_json_file)
        self.lineditStockList=QLineEdit("");
        gridLayout.addWidget(self.btnOpenStockList,0,0);
        gridLayout.addWidget(self.lineditStockList,0,1);
        self.btnOpenIndexList=QPushButton("Open index list");
        self.btnOpenIndexList.clicked.connect(self.select_index_json_file)
        self.lineditIndexList=QLineEdit("");
        gridLayout.addWidget(self.btnOpenIndexList,1,0);
        gridLayout.addWidget(self.lineditIndexList,1,1);
        layout.addLayout(gridLayout);
        
        self.start_button = QPushButton("Start Work");
        self.start_button.clicked.connect(self.start_work);
        layout.addWidget(self.start_button);
        
        self.progress_bar = QProgressBar();
        self.progress_bar.setMinimum(0);
        layout.addWidget(self.progress_bar);
        
        self.table = QTableWidget();
        layout.addWidget(self.table);
        
        self.setLayout(layout)
        self.setGeometry(0, 0, 1600, 250);
        
    def start_work(self):
        fileStock=self.lineditStockList.text();
        fileIndex=self.lineditIndexList.text();
        
        fileStock_exists = os.path.exists(self.lineditStockList.text());
        fileIndex_exists = os.path.exists(self.lineditIndexList.text());
        
        if fileStock_exists and fileIndex_exists:
            stock_data = json.load(open(fileStock));
            index_data = json.load(open(fileIndex));
            
            self.progress_bar.setMaximum(len(stock_data));
            
            self.thread = cwt.WorkerThread(stock_data,index_data,self.table);
            self.thread.update_progress.connect(self.update_progress_bar);
            self.thread.start();
        
        if fileStock_exists==False:
            reply = QMessageBox.question(   self, 
                                            'Error open the stock file', 
                                            "The stock file no exist: "+fileStock,
                                            QMessageBox.Ok);
        
        if fileIndex_exists==False:
            reply = QMessageBox.question(   self, 
                                            'Error open the index file', 
                                            "The index file no exist: "+fileIndex,
                                            QMessageBox.Ok);
    
    def update_progress_bar(self, value):
        self.progress_bar.setValue(value);
    
    def select_stock_json_file(self):
        # Crear un cuadro de diálogo de selección de archivo
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(  self,
                                                    "Seleccionar archivo",
                                                    "",
                                                    "JSON Files (*.stock.json);;All Files (*)",
                                                    options=options);
        if fileName:
            self.lineditStockList.setText(fileName);

    def select_index_json_file(self):
        # Crear un cuadro de diálogo de selección de archivo
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(  self,
                                                    "Seleccionar archivo",
                                                    "",
                                                    "JSON Files (*.index.json);;All Files (*)",
                                                    options=options);
        if fileName:
            self.lineditIndexList.setText(fileName);
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
