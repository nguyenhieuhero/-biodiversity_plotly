import plotly.express as px
import geopandas as gpd
import pandas as pd

world=gpd.read_file("data\countries.geojson")
data=pd.read_csv(r"data\annual-change-forest-area.csv")
full=world.merge(data,left_on=["ISO_A3"],right_on=["Code"])
full=full[full["Year"]==2000]
print(full)
fig = px.choropleth(full,locations="ISO_A3",color="Annual net change in forest area",color_continuous_scale="Viridis",color_continuous_midpoint=0,hover_data=['ADMIN'])
fig.update_layout(title="Deforestation and Forest Loss")
fig.show()