import pandas as pd 
import os 

df1 = pd.read_excel('email_addresses.xlsx')
data1 = pd.DataFrame(df1)
df2 = pd.read_excel('new_excel.xlsx')
data2 = pd.DataFrame(df2)



ls = []

# ls.append(df1)
# ls.append(df2)

# To merge all exel files in the current directory
file_path = './'
for file in os.listdir(file_path):
    if file.endswith(".xlsx"):
        ls.append(pd.read_excel(os.path.join(file_path, file)))

new_file = pd.concat(ls, axis=0)
new_file.to_excel("email_addresses.xlsx", index=False)
