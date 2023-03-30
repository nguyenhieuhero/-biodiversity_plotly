from dash import html
import base64
def header():
    encoded_image = base64.b64encode(open("source/assets/fixbio.png", 'rb').read())
    return html.Div(children=[
        html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),style={'filter': 'drop-shadow(5px 5px 5px white)'}),
    ],style={'padding':'0px',
             'margin':'40px',})