# Import packages
from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

# Incorporate data
df1 = pd.read_csv("goldstock_v1.csv")
df2 = pd.read_csv("Crude_Oil_Data.csv")
df3 = pd.read_csv("SP500.csv")
# Data cleaning
df1["Date"] = pd.to_datetime(df1["Date"]).dt.tz_localize(None)
# Initialize the app
app = Dash()

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
