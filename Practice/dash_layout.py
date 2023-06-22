import pandas as pd
import dash
from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output

# Add DataFrame
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "NYC", "MTL", "NYC"]
})
# Add a bar graph figure
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(
        children='Dashboard',
        style={
            'textAlign': 'center'
        }
    ),
    
    # Create dropdown
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='NYC' # Providing a value to the dropdown
    ),
    
    # Bar graph
    dcc.Graph(id='example-graph-2', figure=fig)
])

# Callback function to update the graph based on dropdown selection
@app.callback(
    Output('example-graph-2', 'figure'),
    Input('dropdown', 'value')
)
def update_graph(city):
    filtered_df = df[df['City'] == city]
    updated_fig = px.bar(filtered_df, x="Fruit", y="Amount", color="City", barmode="group")
    return updated_fig

# Run Application
if __name__ == '__main__':
    app.run_server(debug=True)
