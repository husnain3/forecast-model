import pandas as pd
from prophet import Prophet


moneyIn = './money-in.csv'
moneyOut = './money-out.csv'

# print(moneyIn)

df = pd.read_csv(moneyIn)
df.head()
df