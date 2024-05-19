# This Python file uses the following encoding: utf-8
import sys
import os
import json

from PySide6.QtWidgets import ( QTableWidget,
                                QGridLayout,
                                #QLabel,
                                QLineEdit,
                                QPushButton,
                                QApplication,
                                QVBoxLayout,
                                QFileDialog,
                                QDialog)
    
import stock_table_lib as stlib 

class Form(QDialog):

    def __init__(self, parent=None):
    
        self.RowItem={};

            
        super(Form, self).__init__(parent)
        
        layout = QVBoxLayout();

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

        self.btnGenerate=QPushButton("Generate");
        self.btnGenerate.clicked.connect(self.generate);
        layout.addWidget(self.btnGenerate);

        self.table = QTableWidget();

        layout.addWidget(self.table);
        
        # Set dialog layout
        self.setLayout(layout)
        
        self.setGeometry(0, 0, 1600, 250)
        
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

    def generate(self):
        fileStock=self.lineditStockList.text();
        fileIndex=self.lineditIndexList.text();

        fileStock_exists = os.path.exists(self.lineditStockList.text());
        fileIndex_exists = os.path.exists(self.lineditIndexList.text());


        if fileStock_exists and fileIndex_exists:
            stock_data = json.load(open(fileStock));
            index_data = json.load(open(fileIndex));

            stlib.createTable(self.table,stock_data,stlib.TOTAL_FINANCE_LIST,stlib.FMT_NUM);


if __name__ == "__main__":

    # Opening JSON file 
    

    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
