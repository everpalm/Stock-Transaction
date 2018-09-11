import stock.get_stock as sgs

#sgs.import_data()
#sgs.export_data(2014, 2018, '2330')
#stock_2330 = sgs.MyStock('2330')
stock_2454 = sgs.MyStock('2454')
#stock_2454.export_data(2017, 2018)
#stock_2330.export_data(2014,2018)
#df = stock_2330.import_data('20170101', '20180816')
df = stock_2454.import_data('20170705', '20170707')
print(df)
#sector = stock_2454.average_data('20170701', '20180801')
#print(sector)
#print(df)
