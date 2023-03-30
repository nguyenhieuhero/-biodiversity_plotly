from dash import html
from layout.css import *


def intro():
    return html.Div([
        html.H1("Introduction",style=headerH1),
        html.P("Đa dạng sinh học là khái niệm dùng để mô tả sự đa dạng của các loài sinh vật và môi trường sống của chúng trên Trái đất.",
               style=P1),
        html.Ul([
            html.Li("Nó giúp duy trì cân bằng sinh thái",style=Li1),
            html.Li("Cung cấp nguồn thực phẩm, thuốc và nhiều sản phẩm khác",style=Li1),
            html.Li("Mang lại nhiều lợi ích văn hoá và tâm linh cho con người",style=Li1),
            html.Li("Là nguồn cảm hứng cho nghệ thuật, văn hóa, tôn giáo và các hoạt động giải trí",style=Li1)
            ],style={'width':'70%'}),
        html.P("Tuy nhiên, đa dạng sinh học đang bị suy giảm nghiêm trọng do sự can thiệp của con người vào các hệ sinh thái. Các hoạt động như khai thác rừng, đô thị hóa và sử dụng đất không bền vững đều gây ra mất mát đa dạng sinh học. Ngoài ra, sự biến đổi khí hậu và sự ô nhiễm môi trường cũng đang góp phần vào suy giảm đa dạng sinh học.",
               style=P1)
        
    ],style={'display':'flex',
             'width':'100%',
             'height':'auto',
             'flex-direction':'column',
             'align-items':'center',
             'padding':'0px',
             'margin':'0px'})
