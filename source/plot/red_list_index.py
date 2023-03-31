import pandas as pd
import plotly.express as px


def ril():
    df2 = pd.read_csv(r"data\red-list-index.csv")
    df2 = df2.rename(columns = {'15.5.1 - Red List Index - ER_RSK_LST': 'Index'})
    df2_pivot = df2.pivot(index='Year', columns='Entity', values='Index')
    df2_pivot = df2_pivot.reset_index()
    fig= px.choropleth(df2, 
        locations='Code', 
        color='Index',
        color_continuous_scale= 'viridis',
        animation_frame='Year',
        hover_name='Entity',
        width=1000)
    fig.update_layout(
        title='Red List Index (1993 - 2022)',
        xaxis_title='Year',
        yaxis_title='Index',
    )
    fig.update_coloraxes(
        cmin=0,
        cmax=1
    )
    fig2=px.line(df2_pivot,x='Year',y=['World','Guam', 'Niue','Canada','Sri Lanka','China','Vietnam'],width=1000,markers=True)
    fig2.update_layout(title='Red List Index (1993 - 2022)',
        xaxis_title='Year',
        yaxis_title='Index',
        yaxis=dict(range=[0, 1.0])
        )
    fig3=px.bar(df2,x="Entity",y="Index",animation_frame="Year",width=1000)
    fig3.update_xaxes(
        visible=False
    )
    fig3.update_layout(
        title='World\'s Index over year',
    )
    return [fig,fig2,fig3]
