import plotly
import base64
import dash
from dash import html
from layout.test import test
from layout.header import header
from layout.intro import intro
from dash import dcc
from dash import Input, Output
from plot.forest_loss import forest_loss
from plot.colors.func import get_colors
sea=get_colors("source\plot\colors\sea\sea.txt")
app=dash.Dash()

app.layout=html.Div([
    ],style={'background-color':sea[1],
             'display':'flex',
             'width':'100%',
             'height':'5000px',
             'flex-direction':'column',
             'align-items':'center',
             'outline': 'none',
             'padding':'0px',
             'margin':'0px',
             })


if __name__ == '__main__':
    app.run_server(port=4050,debug=True)