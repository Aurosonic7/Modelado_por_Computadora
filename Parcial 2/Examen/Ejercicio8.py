from PIL import Image
import math

imagen = Image.open('/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 2/Examen/chihuahua.jpg')

ancho, alto = imagen.size

imagen_remolino = Image.new('RGB', (ancho, alto))

centro_x, centro_y = ancho // 2, alto // 2

factor_estiramiento = 1 

for x in range(ancho):
    for y in range(alto):
        distancia = math.sqrt((x - centro_x) ** 2 + (y - centro_y) ** 2)
        if distancia > 0:
            theta = math.atan2(y - centro_y, x - centro_x)
        else:
            theta = 0
        nuevo_x = int(centro_x + distancia * factor_estiramiento * math.cos(theta + distancia / 10))
        nuevo_y = int(centro_y + distancia * factor_estiramiento * math.sin(theta + distancia / 10))
        
        nuevo_x = max(0, min(ancho - 1, nuevo_x))
        nuevo_y = max(0, min(alto - 1, nuevo_y))
        
        color = imagen.getpixel((nuevo_x, nuevo_y))
        
        imagen_remolino.putpixel((x, y), color)

imagen.show()
imagen_remolino.show()