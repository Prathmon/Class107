import csv
import pandas as pd
import plotly.graph_objects as go

file1 = pd.read_csv("data.csv")
roll_no = file1.loc[file1['student_id'] == "TRL_987"]
print(roll_no.groupby("level")["attempt"].mean())
fig = go.Figure(go.Bar(x = roll_no.groupby("level")["attempt"].mean(), y = ["Level 1", "Level 2", "Level 3", "Level 4"],
orientation = 'h'))
fig.show()