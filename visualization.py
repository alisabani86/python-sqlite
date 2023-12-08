import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('my_database.db')



df = pd.read_sql_query("SELECT * from Orders", conn)

df['date'] = pd.to_datetime(df['date'])

df.set_index('date', inplace=True)

monthly_sales = df.groupby('product').resample('M')['amount'].sum()

monthly_sales.unstack().plot()
plt.title('Monthly Sales Trends by Product')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()