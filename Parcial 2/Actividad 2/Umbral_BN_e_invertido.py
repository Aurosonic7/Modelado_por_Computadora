from PIL import Image

Ruta = "/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 2/Actividad 1/mario.jpg"

imagen1 = Image.open(Ruta).convert('L')

imagenbn = Image.new('L',imagen1.size)
imagenbnInv = Image.new('L',imagen1.size)

ancho, alto = imagen1.size

for x in range(ancho):
    for y in range(alto):
        pixel = imagen1.getpixel((x, y))
        if pixel > 128:
            imagenbn.putpixel((x, y), 255)
            imagenbnInv.putpixel((x, y), 0)
        else:
            imagenbn.putpixel((x, y), 0)
            imagenbnInv.putpixel((x, y), 255)

imagenbn.show()
imagenbnInv.show()