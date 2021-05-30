"""
Sanskar Kakde
Email-ID: sanskarkakde13@gmail.com
"""
# Importing required libraries
import folium
import pandas
# Getting the longitude and latitude of all the countries
countries_locations = pandas.read_csv("countries.csv")
population = pandas.read_csv("Populationstats.csv")
lat = list(countries_locations["latitude"])
lon = list(countries_locations["longitude"])
pupltn = list(population["column_b"])
# trying to convert to numeric
lt = pandas.to_numeric(lat)
lg = pandas.to_numeric(lon)
ppl = pandas.to_numeric(pupltn, errors='coerce')
# change popup color depending on population
def icon_color(country_population):
    if country_population <= 100:
        return "blue"
    elif country_population <= 1000:
        return "purple"
    elif country_population <= 10000:
        return "orange"
    elif country_population <= 100000:
        return "darkgreen"
    elif country_population <= 1000000:
        return "beige"
    elif country_population <= 10000000:
        return  "black"
    elif country_population <= 100000000:
        return "darkblue"
    else:
        return "red"
# Looping through the countries 
geo_map = folium.Map(location=[23.52184053531888, 76.58126542592036], zoom_start=3.8)
background = folium.FeatureGroup(name= "Population map")
for lt, lg, ppl in zip(lat, lon, pupltn):
    background.add_child(folium.CircleMarker(location= [lt , lg],radius=6, popup= f"population: {ppl}",fill_color=icon_color(ppl), color='silver', fill_opacity=1.2, icon=folium.Icon(color=icon_color(ppl))))
# Chloropleth
geo_map.add_child(folium.GeoJson(data=(open("Worldcoordinates.json", 'r', encoding='utf-8-sig').read())))
# Rendering
geo_map.add_child(background)
# layer control
geo_map.add_child(folium.LayerControl())
# displaying to the web
geo_map.save("map.html")