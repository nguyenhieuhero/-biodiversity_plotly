from dash import html
from dash import dcc,Input,Output
from layout.css import *
from plot.rhino import brhino
import base64
def body1():
    encoded_image = base64.b64encode(open("source/assets/black_rhino.jpg", 'rb').read())
    return html.Div([
       html.H1("Nguyên nhân cho sự suy giảm Red List Index",style=headerH1),
       html.P("Nạn săn bắt trộm",
              style=P1),
       html.P("Nạn săn bắt trộm là một trong những nguyên nhân chính dẫn đến sự suy giảm của Red List Index của rất nhiều loài đặc biệt là của động vật quý hiếm.",
              style=P2),
       dcc.Dropdown(['Africa', 'Botswana', 'India', 'Kenya', 'Mozambique', 'Namibia', 'Nepal','Zimbabwe'], 'Zimbabwe', id='rhino_cnt',style={'width':'200px','margin-top':'20px'}),
       dcc.Graph(id='rhino',figure={}),
       html.P("Nạn săn trộm đã đẩy các loài tê giác rất gần với bờ vực tuyệt chủng, trong đó phải kể đến tê giác đen",
              style=P2),
       html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),style={'filter':'drop-shadow(5px 5px 5px white)','width':'1400px'}),
       html.P("Trong những năm gần đây, số lượng tê giác đen trên thế giới có lúc đã xuống tới ngưỡng báo động",
               style=P2),
       dcc.Graph(figure=brhino()),
    ],style={'display':'flex',
             'width':'100%',
             'height':'auto',
             'flex-direction':'column',
             'align-items':'center',
             'padding':'0px',
             'margin':'0px'})