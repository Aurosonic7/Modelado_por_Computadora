from PIL import Image
imagen_original = Image.open('/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 2/Examen/chihuahua.jpg')
ancho, alto = imagen_original.size
tamano_filtro = 5
imagen_suavizada = Image.new('RGB', (ancho, alto))
for x in range(ancho):
    for y in range(alto):
        valores_vecinos = []
        for i in range(max(0, x - tamano_filtro // 2), min(ancho, x + tamano_filtro // 2 + 1)):
            for j in range(max(0, y - tamano_filtro // 2), min(alto, y + tamano_filtro // 2 + 1)):
                pixel = imagen_original.getpixel((i, j))
                valores_vecinos.append(pixel)
        r_median = sorted([v[0] for v in valores_vecinos])[len(valores_vecinos) // 2]
        g_median = sorted([v[1] for v in valores_vecinos])[len(valores_vecinos) // 2]
        b_median = sorted([v[2] for v in valores_vecinos])[len(valores_vecinos) // 2]
        imagen_suavizada.putpixel((x, y), (r_median, g_median, b_median))
imagen_original.show()
imagen_suavizada.show()