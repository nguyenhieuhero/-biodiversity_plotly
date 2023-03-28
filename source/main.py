import plotly
import dash
import dash_html_components as html
import dash_core_components as dcc


app=dash.Dash()
app.layout=html.Div([
    html.H1("Hello")
])

if __name__ == '__main__':
    app.run_server(port=4050)