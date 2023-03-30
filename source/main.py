import plotly
import base64
import dash
from dash import html
from layout.test import test
from layout.header import header
from layout.intro import intro
from layout.intro2 import intro2
from layout.body1 import body1
from layout.body2 import body2
from layout.body3 import body3
from dash import dcc
from dash import Input, Output
from plot.rhino import rhino_poached
from plot.colors.func import get_colors

sea=get_colors("source\plot\colors\sea\sea.txt")
app=dash.Dash()

app.layout=html.Div([
    html.Div([
        # header(),
        # intro(),
        # intro2(),
        body1(),
        body2(),
        body3(),
    ],style={'display':'flex',
             'width':'100%',
             'min-height':'5000px',
             'flex-direction':'column',
             'align-items':'center',
             'outline': 'none',
             'padding':'0px',
             'margin':'0px',
             'padding-top':'30px',
             'background-color':'rgba(0,0,0,0.5)'
             }),
    ],style={'background-image': 'url("https://static.wixstatic.com/media/efd012_e1a57f7bf6814483adc631752fdb5566~mv2.png/v1/fill/w_1200,h_611,al_c,q_90,enc_auto/efd012_e1a57f7bf6814483adc631752fdb5566~mv2.png")',
             'background-repeat': 'no-repeat',
             'background-size': 'cover',
             'background-attachment': 'fixed',
             })
@app.callback(
    Output(component_id='rhino', component_property='figure'),
    Input(component_id='rhino_cnt', component_property='value')
)
def update_rhino(cnt):
    return rhino_poached(cnt)


if __name__ == '__main__':
    app.run_server(port=4050,debug=True)