import pandas as pd
import plotly.express as px
def hbt_loss():
    df=pd.read_csv("data\projected-habitat-loss-extent-bau.csv",usecols=["species_losing_more_25pct","species_losing_more_50pct","species_losing_more_75pct","species_losing_more_90pct"])
    df=df.transpose().reset_index()
    df.columns=["Title","Value"]
    df=df.sort_values(by="Value")
    fig=px.bar(df,x="Value",y="Title",orientation='h',text_auto=True,width=1000)
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = [0, 200, 400, 600, 800, 1000, 1200],
            ticktext = ["0 species", "200 species", "400 species", "600 species", "800 species", "1000 species", "1200 species"]
        ),
        yaxis = dict(
            tickmode = 'array',
            tickvals = ["species_losing_more_25pct","species_losing_more_50pct","species_losing_more_75pct","species_losing_more_90pct"],
            ticktext = ["Losing more than 25%","Losing more than 50%","Losing more than 75%","Losing more than 90%"]
        ),
        xaxis_title=None,
        yaxis_title=None,
        title="Number of animal species losing habitat due to cropland expansion by 2050"
    )

    fig.update_traces(marker_color="#21918c")
    return fig
