# InteractiveWorldPopulationMap-(Python+Folium)-
:smile: A python project bases on folium library, making an interactive 2 layered pointer map which gives data about world population country wise.

## Prerequisites :pencil2:
### Libraries required:- :books:
- Folium
- Pandas   
```bash
pip install folium  
pip install pandas  
```  
**Run the above two commands in a shell to install the libraries*
### Files required:- :open_file_folder:
- Populationstats.csv
- Worldcoordinates.json
- countries.csv  
**The above files are available in the repository**  
### IDE/Editor :page_with_curl:
Any IDE/Editor may work which supports python 3.0++, I made this project on PyCharm with Python version 3.8.  
## Description & Usage :closed_book:
Install the required libraries if not, before proceeding forwards.
Copy/type the code from map(code).py in your respective text editor/IDE and save the code.
Paste the above requisite in the directory where the current project is saved.  
(It is done so python may discover the linked files as i have linked directly by placing the file in project's directory, you can place them anywhere but make sure to link them by changing their location inside the code).  
  
#### Function of files
>Worldcoordinates.json - tells python about map locations, it is used here so chloropleth layer of map may highlight the countries based on latitude and longitude.  
>populationstats.csv   - contains the country wise population of the world.(provides population data, since this is an older file you may use updated version from internet). 
>countries.csv         - contain latitude and longitude of countries(folium markers will be placed on them and click popup will display the population data).  
  
A json (Javascipt object notation) - a file used to contain portable data, here data is enclosed in {}, value assignment is done using : and seperation is done using , .  
A csv  (Comma seperated value)     - a file similiar to a .xls file but rather containing tables directly data is seperated using commas , here the first row specifies coloumn headers.  

#### Note :high_brightness:
Marker colors are decided on the basis of a nested if else loop using population data, which are representing the density of population.
```python
background.add_child(folium.CircleMarker(location= [lt , lg],radius=6, popup= f"population: {ppl}",fill_color=icon_color(ppl), color='silver', fill_opacity=1.2, icon=folium.Icon(color=icon_color(ppl))))
```
The file will be saved on desired location and name here it saves in the project directory itself
```python
geo_map.save("map.html")
```
Pre-Loaded zoom level value can be changed
```python
geo_map = folium.Map(location=[23.52184053531888, 76.58126542592036], zoom_start=3.8)
```
### About :grin:
Hello there my name is Sanskar kakde, i am a computer/tech enthusiast (from childhood). Currently doing bachelors degree in computer science enginnering.
I am in learning phase and i made this project to develop my skills. Please report any errors if found and pull requests are welcomed, kindly open an issue first so, i may learn and discuss. 
:relieved:


