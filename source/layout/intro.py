from dash import html
def intro():
    return html.Div([
        html.H1("Introduction"),

    ],style={'display':'flex',
             'width':'100%',
             'height':'auto',
             'flex-direction':'column',
             'align-items':'center',
             'padding':'0px',
             'margin':'0px'})