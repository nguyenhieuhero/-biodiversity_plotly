import plotly.express as px
import geopandas as gpd
import pandas as pd
from colors.func import get_colors

colors=get_colors(r"source\plot\colors\no_yes\ny.txt")
world=gpd.read_file("data\countries.geojson")
data=pd.read_csv(r"data\budget-to-manage-invasive-alien-species.csv")
data.rename(columns={"15.8.1 - Countries with an allocation from the national budget to manage the threat of invasive alien species (1 = YES, 0 = NO) - ER_IAS_NATBUD":"Y"},inplace=True)
data["Y"].replace([0,1],["No","Yes"],inplace=True)
full=world.merge(data,left_on=["ISO_A3"],right_on=["Code"])

print(full)
fig = px.choropleth(full,locations="ISO_A3",color="Y",hover_data=['ADMIN'],color_discrete_sequence=colors)
fig.update_layout(title="Countries with a budget for invasive alien species management, 2020")
fig.show()