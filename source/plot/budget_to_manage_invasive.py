import plotly.express as px
import geopandas as gpd
import pandas as pd
from plot.colors.func import get_colors
def ie():
    colors=get_colors(r"source\plot\colors\no_yes\ny.txt")
    world=gpd.read_file("data\countries.geojson")
    data=pd.read_csv(r"data\budget-to-manage-invasive-alien-species.csv")
    data.rename(columns={"15.8.1 - Countries with an allocation from the national budget to manage the threat of invasive alien species (1 = YES, 0 = NO) - ER_IAS_NATBUD":"Budget for invasive alien species management"},inplace=True)
    data["Budget for invasive alien species management"].replace([0,1],["No","Yes"],inplace=True)
    full=world.merge(data,left_on=["ISO_A3"],right_on=["Code"])
    fig = px.choropleth(full,locations="ISO_A3",color="Budget for invasive alien species management",hover_data=['ADMIN'],color_discrete_sequence=colors,width=1400, height=800)
    fig.update_layout(title="Countries with a budget for invasive alien species management, 2020")
    return fig