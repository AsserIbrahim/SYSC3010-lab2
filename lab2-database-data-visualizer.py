import plotly.express as px
import pandas as pd
import sqlite3

dbconnect = sqlite3.connect("sensorDB.db")

df = pd.read_sql_query(''' SELECT * FROM sensordata''', dbconnect);

fig = px.scatter(df, x='time', y=['temperature', 'humidity', 'pressure'], title='Sensor data')
fig.show()
