import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from app_layout import layout
from data_processing import load_data, preprocess_data
import plotly.express as px



data = load_data()
data = preprocess_data(data)


app = dash.Dash(__name__)


app.layout = layout(data)


@app.callback(
    Output('turbidity-graph', 'figure'),
    [Input('potability-dropdown', 'value')]
)
def update_graph(potability):
    filtered_data = data[data['Potability'] == potability]
    fig = px.histogram(filtered_data, x='Turbidity', title='Turbidity Level Distribution')
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)
