import logging
import requests
import pandas as pd
from datetime import datetime
import json
import sys
import codecs
from time import sleep

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def get_data(trade_date, stock_num):
    logger.debug('trade_date = %s, stock_num = %s', trade_date, stock_num)
    res = requests.get("http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=" + trade_date + "&stockNo=" + stock_num + "&_=1535725086036")
    result = json.loads(res.text)
    df = pd.DataFrame(result['data'])
    df.columns = result['fields']
    return df

def export_data(year_start, year_end, stock_num):
    df = pd.DataFrame()
    for year_count in range(year_start, year_end, 1):
        for month_count in range(1, 13, 1):
            date_count = "{0}{1:02d}01".format(year_count, month_count)
            df_temp = get_data(date_count, stock_num)
            df = df.append(df_temp, ignore_index=True)
            sleep(3)
    print(df)
    df.to_csv(stock_num + '_raw_data.csv', encoding='utf-8')

def import_data(stock_num, date_start, date_end):
    df = pd.read_csv(stock_num + '_raw_data.csv',encoding='utf-8')

    ''' Refactor format of year, month and day
    '''
    year_start = date_start[0:4]
    month_start = date_start[4:6]
    day_start = date_start[6:8]
    year_end = date_end[0:4]
    month_end = date_end[4:6]
    day_end = date_end[6:8]
    
    logger.debug('date_start = %s, year_start = %s, month_start = %s, day_start = %s', date_start, year_start, month_start, day_start)
    logger.debug('date_end = %s, year_end = %s, month_end = %s, day_end = %s', date_end, year_end, month_end, day_end)
    year_start_tw = str(int(year_start) - 1912)
    year_end_tw =  str(int(year_end) - 1912)
    temp = df[(df['日期'] > year_start_tw + '/' + month_start + '/' + day_start) & (df['日期'] < year_end_tw + '/' + month_end + '/' + day_end)]
    return temp

