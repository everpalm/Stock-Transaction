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

def get_stock(trade_date, stock_num):
    logger.debug('trade_date = %s, stock_num = %s', trade_date, stock_num)
    res = requests.get("http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=" + trade_date + "&stockNo=" + stock_num + "&_=1535725086036")
    result = json.loads(res.text)
    df = pd.DataFrame(result['data'])
    df.columns = result['fields']
    return df

df = pd.DataFrame()
for year_count in range(2017, 2018, 1):
    for month_count in range(1, 13, 1):
        date_count = "{0}{1:02d}01".format(year_count, month_count)
        df_temp = get_stock(date_count, "2330")
        df = df.append(df_temp, ignore_index=True)
        sleep(3)
print(df)
