
# Showing the CSV data in dotted graph

import plotly.express as px
import pandas as pd

df = pd.read_csv("employees.csv")

fig = px.scatter(df, x="Salary", y="PerformanceScore", hover_data= ["Name", "Department", "Salary", "Position", "PerformanceScore"])


fig.show()