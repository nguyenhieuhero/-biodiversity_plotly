from dash import html
from dash import dcc
from layout.css import *
from plot.forest_loss import forest_loss
from plot.habitat_loss_2050 import hbt_loss
def body2():
    return html.Div([
       html.H1("Nguy cơ mất môi trường sống",style=headerH1),
       html.P("Sự gia tăng dân số chóng mặt kéo theo nhiều vấn đề về nhu cầu thiết yếu, trong đó vấn đề về lương thực thực phẩm là một trong những vấn đề quan trọng nhất.",style=P1),
       html.P("Để giải quyết vấn đề thực phẩm thì con người đã mở rộng đất canh tác nhằm đáp ứng diện tích trồng trọt cây lương thực; tuy nhiên có rất nhiều hành vi xâm lấn, phá rừng trái phép để sử dụng làm đất canh tác.",style=P2),
       dcc.Graph(figure=forest_loss()),
       html.P("Điều này ảnh hưởng không nhỏ đến môi trường không chỉ đến con người mà đến cả hệ sinh thái khi các sinh vật trú ấn trong rừng bị mất môi trường sống dẫn đến suy giảm số lượng hay có thể là biến mất khỏi vị trí đó",style=P2),
       dcc.Graph(figure=hbt_loss())
    ],style={'display':'flex',
             'width':'100%',
             'height':'auto',
             'flex-direction':'column',
             'align-items':'center',
             'padding':'0px',
             'margin':'0px'})