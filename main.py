import logging
import stock.get_stock as sgs

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

#sgs.import_data()
#sgs.export_data(2014, 2018, '2330')
#stock_2330 = sgs.MyStock('2330')
stock_2454 = sgs.MyStock('2454')
#stock_2454.export_data(2017, 2018)
#stock_2330.export_data(2014,2018)
#df = stock_2330.import_data('20170101', '20180816')
df = stock_2454.import_data('20170705', '20170707')
print(df)
#print(len(df['漲跌價差']))
'''
df_length = len(df['漲跌價差'])
row_num = 0
for series_element in df['漲跌價差']:
    logger.debug('Before series_element = %s', series_element)
    if series_element == 'X0.00':
        series_element = series_element.replace('X','')
    series_element = float(series_element)
    print(series_element)
    logger.debug('After series_element = %f', series_element)
'''
#df['漲跌價差'].values = df['漲跌價差'].values.astype(float)
#df['漲跌價差'].values = df['漲跌價差'].replace('X0.00','0')
#print(df['漲跌價差'].values)
#sector = stock_2454.average_data('20170701', '20180801')
#print(sector)
#print(df)
