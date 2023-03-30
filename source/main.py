import plotly
import base64
import dash
from dash import html
from dash import dcc
from dash import Input, Output
from plot.forest_loss import forest_loss
from plot.colors.func import get_colors

sea=get_colors("source\plot\colors\sea\sea.txt")
encoded_image = base64.b64encode(open("source/assets/fixbio.png", 'rb').read())

app=dash.Dash()

app.layout=html.Div([html.H1("elu"),
    html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode())),
    dcc.Dropdown([1990, 2000, 2010,2015], 1990, id='dfr-years'),
    dcc.Graph(id='dfr',
              figure={},
              style={'height':'800px',
                     'width':'100%'
                    }),
    html.H1("hoho")
    ],style={'background-color':sea[1],
             'display':'flex',
             'flex-direction':'column'})
@app.callback(
    Output(component_id='dfr',component_property='figure'),
    Input(component_id='dfr-years',component_property='value')
)
def update_graph(value):
    return forest_loss(year=value)



if __name__ == '__main__':
    app.run_server(port=4050,debug=True)