# dashboard_macro.py
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html

# ---------------------------
# Load your cleaned data
# ---------------------------
data_path = "C:/Users/USER/OneDrive/Desktop/projects/macroguard/data/cleaned and standardized data/macro_data.csv"
df = pd.read_csv(data_path, parse_dates=['date'])

# Keep only columns we can visualize
df = df[['date', 'fuel_price_usd', 'inflation_rate']].copy()

# ---------------------------
# Initialize Dash app
# ---------------------------
app = Dash(__name__)
app.title = "Macro Dashboard"

# ---------------------------
# Create figures
# ---------------------------
# Fuel price over time
fig_fuel = px.line(
    df,
    x='date',
    y='fuel_price_usd',
    title='Fuel Prices Over Time',
    labels={'fuel_price_usd': 'Fuel Price (USD)', 'date': 'Date'},
    color_discrete_sequence=['#FF69B4']  # Pink
)
fig_fuel.update_traces(line=dict(width=3))
fig_fuel.update_layout(template='plotly_white')

# Inflation over time
fig_inflation = px.line(
    df,
    x='date',
    y='inflation_rate',
    title='Inflation Rate Over Time',
    labels={'inflation_rate': 'Inflation Rate (%)', 'date': 'Date'},
    color_discrete_sequence=['#800080']  # Purple
)
fig_inflation.update_traces(line=dict(width=3))
fig_inflation.update_layout(template='plotly_white')

# Correlation heatmap
corr_df = df.corr()
fig_corr = go.Figure(
    data=go.Heatmap(
        z=corr_df.values,
        x=corr_df.columns,
        y=corr_df.columns,
        colorscale='PuRd',  # Purple-pink gradient
        zmin=-1,
        zmax=1
    )
)
fig_corr.update_layout(
    title='Correlation Heatmap',
    template='plotly_white'
)

# ---------------------------
# Layout
# ---------------------------
app.layout = html.Div(
    style={'backgroundColor': '#F9F9F9', 'fontFamily': 'Arial, sans-serif', 'padding': '20px'},
    children=[
        html.H1("Macro Dashboard", style={'textAlign': 'center', 'color': '#4B0082'}),

        html.Div([
            dcc.Graph(figure=fig_fuel),
            dcc.Graph(figure=fig_inflation),
            dcc.Graph(figure=fig_corr)
        ])
    ]
)

# ---------------------------
# Run app
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)
