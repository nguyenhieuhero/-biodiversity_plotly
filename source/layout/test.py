from dash import html
from dash import dcc
from plot.forest_loss import forest_loss
import base64
from plot.colors.func import get_colors

def test():
    return html.Div(children=[html.H1("elu"),
    # dcc.Dropdown([1990, 2000, 2010,2015], 1990, id='dfr-years'),
    dcc.Graph(id='dfr',
              figure=forest_loss(),
              style={'height':'800px',
                     'width':'100%'
                    }),
    html.H1("hoho")
    ],style={'padding':'0px',
             'margin':'0px',})
