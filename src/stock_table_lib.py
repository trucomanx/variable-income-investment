
from PySide6.QtWidgets import QTableWidget
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QHeaderView
from PySide6.QtGui     import QBrush
import yfinance as yf

FMT_NUM="%.2f";
TOTAL_FINANCE_LIST=[
    {
        "cmd":"longName",
        "title":"Long name",
        "func":lambda a,b: str(a),
    },
    {
        "cmd":"currentPrice",
        "title":"Price",
        "func":lambda a,b: FMT_NUM%(a),
    },
    {
        "cmd":"currentPrice",
        "title":"Initial amount",
        "func":lambda a,b: FMT_NUM%(b[1]*b[2]),
    },
    {
        "cmd":"currentPrice",
        "title":"Gain",
        "func":lambda a,b: FMT_NUM%(a*b[1]-b[1]*b[2]),
    },
    {
        "cmd":"currentPrice",
        "title":"Gain%",
        "func":lambda a,b: FMT_NUM%((a*b[1]-b[1]*b[2])*100.0/(b[1]*b[2])),
    },
    {
        "cmd":"currentPrice",
        "title":"Final amount",
        "func":lambda a,b: FMT_NUM%(a*b[1]),
    },
    {
        "cmd":"trailingAnnualDividendYield",
        "title":"DY% 1yr",
        "func":lambda a,b: FMT_NUM%(a*100),
    },
    {
        "cmd":"priceToBook",
        "title":"P/BV",
        "func":lambda a,b: FMT_NUM%(a),
    },
    {
        "cmd":"returnOnEquity",
        "title":"ROE%",
        "func":lambda a,b: FMT_NUM%(a*100),
    },
    {
        "cmd":"returnOnAssets",
        "title":"ROA%",
        "func":lambda a,b: FMT_NUM%(a*100),
    },
    {
        "cmd":"enterpriseToRevenue",
        "title":"EV/R",
        "func":lambda a,b: FMT_NUM%(a),
    },    
    {
        "cmd":"trailingPE",
        "title":"P/E",
        "func":lambda a,b: FMT_NUM%(a),
    },
    {
        "cmd":"trailingEps",
        "title":"EPS",
        "func":lambda a,b: FMT_NUM%(a),
    },
    {
        "cmd":"payoutRatio",
        "title":"Payout%",
        "func":lambda a,b: FMT_NUM%(a*100),
    }
];

def createTable(stock_data,finance_list,fmt_num,color_data="#FFFDD0"): 

    title_list=["Name","Qty","Av.Price"];
    
    for item in finance_list:
        title_list.append(item["title"]);
    
    tableWidget = QTableWidget() ;

    #Row count 
    tableWidget.setRowCount(len(stock_data.keys())) ; 
    #Column count 
    tableWidget.setColumnCount(len(title_list));
    
    tableWidget.setHorizontalHeaderLabels(title_list)
    
    n=0;
    for stock_name in stock_data:
        basic_data=[
            stock_name,
            stock_data[stock_name]["qty"],
            stock_data[stock_name]["average-price"]
        ];
        
        witem=QTableWidgetItem(basic_data[0]);
        witem.setBackground(QBrush(color_data));
        tableWidget.setItem(n,0, witem);
        
        witem=QTableWidgetItem(str(basic_data[1]));
        witem.setBackground(QBrush(color_data));
        tableWidget.setItem(n,1, witem);
        
        witem=QTableWidgetItem(fmt_num%(basic_data[2]));
        witem.setBackground(QBrush(color_data));
        tableWidget.setItem(n,2, witem);
        
        ## yfinance
        stock_obj=yf.Ticker(stock_name);
        
        m=0;
        for item in finance_list:
            if item["cmd"] in stock_obj.info:
                item_str=item["func"](stock_obj.info[item["cmd"]],basic_data);
            else:
                item_str='';
            tableWidget.setItem(n,3+m, QTableWidgetItem(item_str));
            m=m+1;
        
        n=n+1;
    
    #Table will fit the screen horizontally 
    #tableWidget.horizontalHeader().setStretchLastSection(True) 
    tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
    
    tableWidget.setStyleSheet("background-color: #E8E8E8")
    
    return tableWidget

