from tracemalloc import start
import numpy as np
import random
import quandl
import pandas as pd
from pandas_datareader import data as wb


def singStock(marker, dataSource, startDate):
    stockInfo = wb.DataReader(marker, data_source= dataSource, start= startDate)['Adj Close']
    return stockInfo

def finDataToCSV(neededData):
    allData = pd.DataFrame()
    markers = neededData['markers']
    srce = neededData['source']
    startDate = neededData['date']

    for i in markers:
        allData[i] = singStock(i, srce, startDate)

    allData.tail(5).to_csv(r'C:\Users\infin\OneDrive\Documentos\Python for Finance\my_data02.csv')

def finDataToExcel(neededData):
    allData = pd.DataFrame()
    markers = neededData['markers']
    srce = neededData['source']
    startDate = neededData['date']

    for i in markers:
        allData[i] = singStock(i, srce, startDate)

    allData.tail(5).to_excel(r'C:\Users\infin\OneDrive\Documentos\Python for Finance\my_data02.xlsx')

def finDataToJson(neededData):
    allData = pd.DataFrame()
    markers = neededData['markers']
    srce = neededData['source']
    startDate = neededData['date']

    for i in markers:
        allData[i] = singStock(i, srce, startDate)

    allData.tail(5).to_json(r'C:\Users\infin\OneDrive\Documentos\Python for Finance\my_data02.json')


neededData = {'markers': ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'GOOG', 'TSLA', 'UNH', 'JNJ', 'NVDA'], 'source': 'yahoo', 'date': '2022-1-1'}

finDataToCSV(neededData)
finDataToExcel(neededData)
finDataToJson(neededData)
