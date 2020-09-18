import pandas as pd

df = pd.read_csv('https://docs.google.com/spreadsheets/d/1Fn3j0jgMumjx_RK_vACYm27T7XaCnaPqiHGayorcxFw/export?format=csv', dtype=object)
df.rename(mapper={'Số Lượng Căn Hộ':'Quantity'},inplace=True, axis=1)
df.to_csv('CC_Address - HN_HY_HCM.csv', index=False)
print('Downloaded')