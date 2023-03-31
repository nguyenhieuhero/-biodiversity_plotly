from dash import html
from dash import dcc
from layout.css import *

def end():
    return html.Div([
       html.H1("Ý nghĩa",style=headerH1),
       html.P("Đa dạng sinh học là yếu tố quyết định tính ổn định và là cơ sở sinh tồn của sự sống cho trái đất và của các hệ sinh thái tự nhiên. Bởi vì nó làm cân bằng số lượng cá thể giữa các loài và đảm bảo cho khống chế sinh học cho các loài với cá thể được tiếp nhận trong hệ sinh thái.",style=P2),
      html.P("Chính bởi tầm quan trọng như vậy, bảo vệ sự đa dạng sinh học đóng vai trò quyết định cho sự phát triển không chỉ của các loài động thực vật mà còn của con người chúng ta.",style=P2),

    ],style={'display':'flex',
             'width':'100%',
             'height':'1000px',
             'flex-direction':'column',
             'align-items':'center',
             'padding':'0px',
             'margin':'0px'})