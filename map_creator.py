import folium

# Initialize the map. We'll start at a neutral point for visualization purposes.
m = folium.Map(location=[20, 0], zoom_start=2)

# Define the locations
locations = {
    'Northern Peru': (-15.860541, -47.872291),
    'Meso America': (37.319006, -121.947926),
    'Mesopotamia': (50.744575, 3.600652),
    'Egypt': (26.4941838299718, 29.871903452398),
    'China': (35.4867029846329, 101.901875103385)
}

# Add markers for each location
for location, coordinates in locations.items():
    folium.Marker(
        location=coordinates,
        popup=location,
        icon=folium.Icon(icon='cloud')
    ).add_to(m)

# Save map to an HTML file
m.save("map.html")

# If you want to display the map in Jupyter or IPython environment, simply use:
# m

# To view the map, open "map.html" in a web browser.