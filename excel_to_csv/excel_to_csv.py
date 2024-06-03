
# Below code will convert excel file to csv file

import pandas as pd

data1 = pd.read_excel('europe.xlsx')

data2 = pd.DataFrame(data1)

data2.to_csv('europe.csv')