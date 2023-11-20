from PIL import Image

imagen_original = Image.open('/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 2/Examen/chihuahua.jpg')

niveles_posterizacion = 3 

ancho, alto = imagen_original.size

imagen_posterizada = Image.new('RGB', (ancho, alto))

intervalo = 256 // niveles_posterizacion
rangos = [(i, i + intervalo) for i in range(0, 256, intervalo)]

for x in range(ancho):
    for y in range(alto):
        color_original = imagen_original.getpixel((x, y))

        r, g, b = color_original
        r = min(r // intervalo * intervalo, 255)
        g = min(g // intervalo * intervalo, 255)
        b = min(b // intervalo * intervalo, 255)

        imagen_posterizada.putpixel((x, y), (r, g, b))

imagen_original.show()
imagen_posterizada.show()