import folium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Coordonnées des étapes du 4L Trophy 2025
stages = [
    {"location": (43.9528, 2.8885), "description": "Départ à Saint-Affrique", "date": "19 février 2025"},
    {"location": (43.4831519, -1.558626), "description": "Village Départ à Biarritz", "date": "19-20 février 2025"},
    {"location": (36.1408, -5.3536), "description": "Liaison libre vers Algeciras", "date": "21-22 février 2025"},
    {"location": (35.7595, -5.833954), "description": "Passage du détroit de Gibraltar en bateau", "date": "22-23 février 2025"},
    {"location": (34.020882, -6.841650), "description": "Première étape au Maroc à Rabat", "date": "24 février 2025"},
    {"location": (32.881, -4.963), "description": "Deuxième étape à Boulajoul", "date": "25 février 2025"},
    {"location": (31.0802, -4.0105), "description": "Troisième étape à Merzouga", "date": "26 février 2025"},
    {"location": (31.9356, -4.4699), "description": "Quatrième étape à Oued Ziz", "date": "27 février 2025"},
    {"location": (31.149, -4.005), "description": "Cinquième étape à Erg Chebbi", "date": "28 février 2025"},
    {"location": (31.6295, -7.9811), "description": "Arrivée et remise des prix à Marrakech", "date": "1er mars 2025"}
]

# Créer une carte centrée sur le Maroc en vue satellite
m = folium.Map(location=[31.7917, -7.0926], zoom_start=6, tiles=None)
folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', 
                 attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community').add_to(m)

# Ajouter les marqueurs numérotés pour les étapes avec des icônes personnalisées
for i, stage in enumerate(stages, 1):
    coords = stage["location"]
    description = stage["description"]
    date = stage["date"]
    folium.Marker(
        location=coords,
        popup=f"<strong>{i}. {description}</strong><br>Date : {date}",
        icon=folium.Icon(icon='info-sign', color='blue')
    ).add_to(m)

# Sauvegarder la carte dans un fichier HTML
html_file = "4L_Trophy_2025_Itineraire.html"
m.save(html_file)

# Utiliser Selenium pour capturer une image de la carte (facultatif)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1200x800")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(f"file:///{html_file}")

# Attendre que la carte se charge complètement
time.sleep(5)

# Capturer la carte en tant qu'image (facultatif)
map_png = "4L_Trophy_2025_Itineraire.png"
driver.save_screenshot(map_png)
driver.quit()

# Ouvrir l'image et la sauvegarder au format désiré (facultatif)
img = Image.open(map_png)
img.show()
