import pandas as pd
import pdb

df = pd.read_csv("herc_rentals.csv")

df['Price /day'] = df['Price /day'].str.split("/day")[0][0].replace('$','')

df['Price /week'] = df['Price /week'].str.split("/week")[0][0].replace('$','').replace(',','')
df['Price /month'] = df['Price /month'].str.split("/month")[0][0].replace('$','').replace(',','')

df.to_csv("herc_rentals_cleaned.csv", index=False)

