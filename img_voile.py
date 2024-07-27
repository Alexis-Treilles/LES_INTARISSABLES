from PIL import Image, ImageEnhance

def recadrer_et_ajouter_voile(image_path, output_path):
    # Charger l'image
    image = Image.open(image_path)
    
    # Taille souhaitée
    target_size = (1563, 1135)
    
    # Recadrer l'image
    image_cropped = image.resize(target_size, Image.Resampling.LANCZOS)
    
    # Créer un voile gris avec alpha
    voile = Image.new('RGBA', target_size, (128, 128, 128, int(255 * 0.85)))
    
    # Combiner les images
    image_with_voile = Image.alpha_composite(image_cropped.convert('RGBA'), voile)
    
    # Sauvegarder l'image résultante
    image_with_voile.save(output_path, format="PNG")

# Chemin vers l'image d'entrée et l'image de sortie
image_path = 'img/voiture (2).jpg'
output_path = 'img/TBG01.png'

# Appel de la fonction
recadrer_et_ajouter_voile(image_path, output_path)
