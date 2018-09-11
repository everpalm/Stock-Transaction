import logging
import requests
import pandas as pd
from datetime import datetime
import json
import sys
import codecs
from time import sleep
import matplotlib.pyplot as plt

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.CRITICAL)

logger = logging.getLogger(__name__)

class MyStock:
    def __init__(self, stock_num):
        self.stock_num = stock_num

    def get_data(self, trade_date):
        logger.debug('trade_date = %s, stock_num = %s', trade_date, self.stock_num)
        res = requests.get("http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=" + trade_date + "&stockNo=" + self.stock_num + "&_=1535725086036")
        result = json.loads(res.text)
        df = pd.DataFrame(result['data'])
        df.columns = result['fields']
        return df

    def export_data(self, year_start, year_end):
        df = pd.DataFrame()
        for year_count in range(year_start, year_end, 1):
            for month_count in range(1, 13, 1):
                date_count = "{0}{1:02d}01".format(year_count, month_count)
                df_temp = self.get_data(date_count)
                #df_temp = df_temp.replace('+','')
                #df_temp = df_temp['漲跌價差']
                #df_temp = df_temp['漲跌價差'].values
                #df_temp = df_temp['漲跌價差'].replace('X0.00','0')
                #df_temp = df_temp['漲跌價差'].apply(pd.to_numeric, errors='ignore')
                #logger.debug('df_temp = %s', df_temp)
                #df_temp = df_temp['漲跌價差'].str.replace('+','')
                #logger.debug('df_temp = %s', df_temp['漲跌價差'])
                #df_temp = df_temp['漲跌價差'].replace('X','')
                df = df.append(df_temp, ignore_index=True)
                sleep(3)
        print(df)
        df.to_csv(self.stock_num + '_raw_data.csv', encoding='utf-8')

    def import_data(self, date_start, date_end):
        df = pd.read_csv(self.stock_num + '_raw_data.csv',encoding='utf-8')

        ''' Refactor format of year, month and day '''
        year_start = date_start[0:4]
        month_start = date_start[4:6]
        day_start = date_start[6:8]
        year_end = date_end[0:4]
        month_end = date_end[4:6]
        day_end = date_end[6:8]
    
        year_start_tw = str(int(year_start) - 1911)
        year_end_tw =  str(int(year_end) - 1911)
        logger.debug('date_start = %s, year_start_tw = %s, month_start = %s, day_start = %s', date_start, year_start_tw, month_start, day_start)
        logger.debug('date_end = %s, year_end_tw = %s, month_end = %s, day_end = %s', date_end, year_end_tw, month_end, day_end)
        temp = df[(df['日期'] >= year_start_tw + '/' + month_start + '/' + day_start) & (df['日期'] <= year_end_tw + '/' + month_end + '/' + day_end)]
        return temp

    def average_data(self, date_start, date_end):
        df = self.import_data(date_start, date_end)
        #print(df)
        del df['Unnamed: 0']
        print(df)
        df.groupby('漲跌價差').mean()
        return df
