#imagen_path = "/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 1/gato.jpeg"
from PIL import Image

# Ruta de la imagen de entrada
imagen_path = "/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 1/gato.jpeg"

# Abrir la imagen
imagen = Image.open(imagen_path)
ancho, alto = imagen.size
pixeles = imagen.load()

# Definir el color azul (R, G, B)
color_azul = (0, 0, 255)

# Dibujar las líneas azules en forma de "X" que cubren toda la imagen
for y in range(alto):
    for x in range(ancho):
        if x == y or x == ancho - y - 1:
            pixeles[x, y] = color_azul

# Encontrar las coordenadas de recorte
min_x = ancho
max_x = 0
min_y = alto
max_y = 0

for y in range(alto):
    for x in range(ancho):
        if pixeles[x, y] != color_azul:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

# Recortar la imagen para eliminar el área con líneas azules
imagen_recortada = imagen.crop((min_x, min_y, max_x + 1, max_y + 1))

# Guardar la imagen recortada
imagen_recortada.show()
