from dash import html
from dash import dcc
from layout.css import *
from plot.wl_ep import wl_ep
def body4():
    return html.Div([
       html.H1("Xuất khẩu động vật hoang dã",style=headerH1),
       html.P("Xuất khẩu động vật hoang dã cũng là một trong những yếu tố ảnh hưởng đến đa dạng sinh vật",style=P2),
       dcc.Graph(figure=wl_ep())
    ],style={'display':'flex',
             'width':'100%',
             'height':'auto',
             'flex-direction':'column',
             'align-items':'center',
             'padding':'0px',
             'margin':'0px'})