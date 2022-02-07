import pandas as pd
import csv
import plotly.graph_objects as go

file1 = pd.read_csv("data.csv")
print(file1.groupby("level")["attempt"].mean())
fig = go.Figure(go.Bar(x = file1.groupby("level")["attempt"].mean(), y = ["Level 1", "Level 2", "Level 3", "Level 4"],
 orientation = 'h'))
fig.show()