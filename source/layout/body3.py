from dash import html
from dash import dcc
from layout.css import *
from plot.budget_to_manage_invasive import ie
from plot.habitat_loss_2050 import hbt_loss
def body3():
    return html.Div([
       html.H1("Sự xâm lấn của sinh vật ngoại lai",style=headerH1),
       html.P("Sự xâm lấn của sinh vật ngoại lai là một loại sinh vật đã thích nghi, phát triển, tăng nhanh số lượng cá thể trong hệ sinh thái hoặc nơi sống mới và là nguyên nhân gây ra sự thay đổi về cấu trúc quần xã, đe dọa đến đa dạng sinh học bản địa.",style=P2),
       html.P("Một trong những ví dụ điển hình không thể kể tới là câu chuyện về 24 con thỏ hủy hoại nền kinh tế Úc",style=P2),
       html.P("Để ngăn chặn việc này thì một số quốc gia đã có những quỹ, chính sách để phòng ngừa sinh vật ngoại lại xâm lấn",style=P2),
       dcc.Graph(figure=ie())
    ],style={'display':'flex',
             'width':'100%',
             'height':'auto',
             'flex-direction':'column',
             'align-items':'center',
             'padding':'0px',
             'margin':'0px'})