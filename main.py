import stock.get_stock as sgs

#sgs.import_data()
df = sgs.import_data('2330', '20180101', '20180116')
print(df)
