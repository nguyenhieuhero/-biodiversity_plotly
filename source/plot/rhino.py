import pandas as pd
import plotly.express as px
def rhino_poached(cnt):
    df=pd.read_csv(r"data\number-of-rhinos-poached.csv")
    df=df[df["Entity"]==cnt]
    fig=px.bar(df,x="Year",y="Rhinos Poached (AfRSG, 2019)",width=1400, height=900)
    fig.update_layout(
        title=f"Biểu đồ cột thể hiện số lần tê giác bị săn của {cnt} qua các năm."
    )
    return fig
def brhino():
    df=pd.read_csv(r"data\black-rhinos.csv")
    w=df[df['Entity']=="World"]
    fig2=px.line(w,x="Year",y="Black Rhino population (AfRSG & other sources, 2019)",width=1400, height=900)
    fig2.update_layout(
            title=f"Số lượng tê giác đen trên thế giới qua các năm"
        )
    return fig2