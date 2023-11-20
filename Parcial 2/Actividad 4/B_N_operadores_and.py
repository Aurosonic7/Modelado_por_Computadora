from PIL import Image
imagen1 = Image.open("/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 2/Actividad 3/dbz.jpg")
imagen2 = Image.open("/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 2/Actividad 3/fondo.jpg")

if imagen1.size != imagen2.size:
    print("Las imágenes no tienen el mismo tamaño. No se pueden sumar.")
else:

    imagen1_neg = Image.new('L', imagen1.size)
    imagen2_neg = Image.new('L', imagen2.size)
    resultado = Image.new('L', imagen1.size)

    ancho, alto = imagen1.size

    for x in range(ancho):
        for y in range(alto):
            pixel = imagen1.getpixel((x, y))
            gris = int((pixel[0] + pixel[1] + pixel[2]) / 3)
            if gris > 128:
                imagen1_neg.putpixel((x, y), 255)
            else:
                imagen1_neg.putpixel((x, y), 0)

    for x in range(ancho):
        for y in range(alto):
            pixel = imagen2.getpixel((x, y))
            gris = int((pixel[0] + pixel[1] + pixel[2]) / 3)
            if gris > 128:
                imagen2_neg.putpixel((x, y), 255)
            else:
                imagen2_neg.putpixel((x, y), 0)

    for x in range(ancho):
        for y in range(alto):
            pixel1 = imagen1_neg.getpixel((x, y))
            pixel2 = imagen2_neg.getpixel((x, y))
            color = pixel1 and pixel2
            if color == 0:
                resultado.putpixel((x, y), 0)
            else:
                resultado.putpixel((x, y), 255)

    imagen1_neg.show()
    imagen2_neg.show()
    resultado.show()