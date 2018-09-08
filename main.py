import stock.get_stock as sgs

#sgs.import_data()
#sgs.export_data(2014, 2018, '2330')
df = sgs.import_data('2330', '20170101', '20180816')
print(df)
