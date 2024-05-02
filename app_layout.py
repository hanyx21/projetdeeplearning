from dash import html, dcc
import plotly.express as px

def layout(data):
    fig_pH = px.histogram(data, x='ph', title='pH Level Distribution')
    fig_pH.update_layout(bargap=0.2)
    

    fig_turbidity_placeholder = px.scatter(title="Turbidity Visualization Placeholder")
    
    return html.Div([
        html.H1("Water Quality Dashboard"),
        dcc.Graph(figure=fig_pH),
        dcc.Dropdown(
            id='potability-dropdown',
            options=[{'label': 'Potable', 'value': 1}, {'label': 'Not Potable', 'value': 0}],
            value=1,  # Default value set to 'Potable'
            clearable=False,
        ),
        dcc.Graph(id='turbidity-graph', figure=fig_turbidity_placeholder)
    ])
