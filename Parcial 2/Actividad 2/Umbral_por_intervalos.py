from PIL import Image

Ruta = "/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 2/Actividad 1/mario.jpg"
imagen1 = Image.open(Ruta).convert('L')

intervalo_inferior = 128
intervalo_superior = 255

imaInt = Image.new('L', imagen1.size)

ancho, alto = imagen1.size

for x in range(ancho):
    for y in range(alto):
        pixel = imagen1.getpixel((x, y))
        if intervalo_inferior <= pixel <= intervalo_superior:
            imaInt.putpixel((x, y), 255)
        else:
            imaInt.putpixel((x, y), 0)

imaInt.show()