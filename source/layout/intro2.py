from dash import html
from dash import dcc
from layout.css import *
from plot.red_list_index import ril

def intro2():
    return html.Div([
        html.H1("Red List Index",style=headerH1),
        html.P("Red List Index là 1 thước đo nguy cơ tuyệt chủng của các loài nằm trong danh sách đỏ của Liên minh Bảo tồn Thiên nhiên Quốc tế",
               style=P1),
        html.P("Red List Index là một chỉ số từ 0 đến 1, chỉ số này cảng giảm cho thấy nguy cơ tuyệt chủng của các loài có trong chỉ số đang gia tăng",
               style=P1),
        dcc.Graph(figure=ril()[0]),
        html.P("Sự thay đổi của Red List Index trên thế giới",
               style=P1),
        dcc.Graph(figure=ril()[1]),
        html.P("Biểu đồ cột sự thay đổi của Red List Index trên thế giới",
               style=P1),
        dcc.Graph(figure=ril()[2]),
        
    ],style={'display':'flex',
             'width':'100%',
             'height':'auto',
             'flex-direction':'column',
             'align-items':'center',
             'padding':'0px',
             'margin':'0px'})
