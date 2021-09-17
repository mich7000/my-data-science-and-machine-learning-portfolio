
attr1.to_csv('data/ATTR1.csv')
attr2.to_csv('data/ATTR2.csv')

attr1 = tbl.groupby(['NODE_1', 'ATTR_1'])['NODE_1'].nunique()
attr2 = tbl.groupby(['NODE_2', 'ATTR_2'])['NODE_2'].nunique()