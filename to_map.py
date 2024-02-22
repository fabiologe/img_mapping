import plotly.express as px
import pandas as pd 

data = pd.read_csv("extracted_data.csv")

import plotly.express as px

# Assuming your data has 'Zone' column like in your previous example
zones = data['Zone'].unique()  # Extract unique zones
center_zone = zones[0]  # Choose a representative zone for center (you can adjust)
mapbox_style = f"mapbox://styles/mapbox/{center_zone}-satellite-v9"
# Define UTM32 projection and center coordinates
projection = f"EPSG:326{center_zone}"
center_x, center_y = data[data['Zone'] == center_zone][['Easting', 'Northing']].mean()

# Create map using Plotly Express
m = px.scatter_mapbox(
    data,
    lat=data['Northing'],
    lon=data['Easting'],
    custom_data=[f"<a href='img/{filename}'>View Image</a>" for filename in data['Filename']],
    mapbox_gl=True,
    center={"lat": center_y, "lon": center_x},
    zoom=10,
    projection=projection,
)

# Add custom layers or styling as needed (optional)
# ...

# Show the map
m.show()