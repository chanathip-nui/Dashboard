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
df1["Date"] = pd.to_datetime(df1["Date"], utc=True).dt.tz_localize(None)
df2["Date"] = pd.to_datetime(df2["Date"], utc=True).dt.tz_localize(None)
df3["Date"] = pd.to_datetime(df3["Date"], utc=True).dt.tz_localize(None)

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div(
    [
        html.H1(
            "Financial Market Dashboard",
            style={"textAlign": "center", "fontFamily": "Arial"},
        ),
        html.Div(
            [
                html.Label(
                    "Select an Asset:",
                    style={"fontWeight": "bold", "fontFamily": "Arial"},
                ),
                dcc.Dropdown(
                    id="asset-dropdown",
                    options=[
                        {"label": "Gold Stock", "value": "gold"},
                        {"label": "Crude Oil", "value": "oil"},
                        {"label": "S&P 500", "value": "sp500"},
                    ],
                    value="gold",
                    clearable=False,
                ),
            ],
            style={"width": "40%", "margin": "0 auto", "paddingBottom": "20px"},
        ),
        dcc.Graph(id="price-graph"),
    ]
)


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
