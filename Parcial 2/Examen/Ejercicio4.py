from PIL import Image
def aplicar_filtro_sepia(imagen):
    imagen_gris = imagen.convert('L')
    imagen_sepia = Image.new('RGB', imagen.size)
    pixeles_original = imagen.load()
    pixeles_sepia = imagen_sepia.load()
    matriz_sepia = [
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ]
    for y in range(imagen.height):
        for x in range(imagen.width):
            gris = imagen_gris.getpixel((x, y))
            r, g, b = pixeles_original[x, y]
            nuevo_r = int(r * matriz_sepia[0][0] + g * matriz_sepia[0][1] + b * matriz_sepia[0][2])
            nuevo_g = int(r * matriz_sepia[1][0] + g * matriz_sepia[1][1] + b * matriz_sepia[1][2])
            nuevo_b = int(r * matriz_sepia[2][0] + g * matriz_sepia[2][1] + b * matriz_sepia[2][2])
            pixeles_sepia[x, y] = (nuevo_r, nuevo_g, nuevo_b)
    return imagen_sepia
imagen_original = Image.open('/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 2/Examen/chihuahua.jpg')
imagen_con_filtro_sepia = aplicar_filtro_sepia(imagen_original)
imagen_con_filtro_sepia.show()