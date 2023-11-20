from PIL import Image

Ruta = "/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 2/Actividad 3/fondo.jpg"
imagen1 = Image.open(Ruta)
imagen1.show()
ancho, alto = imagen1.size
Ruta2 = "/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 2/Actividad 3/dbz.jpg"
imagen2 = Image.open(Ruta2)
imagen2.show()
ancho2, alto2 = imagen2.size

if (imagen1.size and imagen2.size):
    newImagenSuma = Image.new('RGB', (ancho, alto))
    newImagenResta = Image.new('RGB', (ancho, alto))

    datos_pixeles = imagen1.load()
    datos_pixeles2 = imagen2.load()
    for x in range(ancho):
        for y in range(alto): 
            pixel = datos_pixeles[x, y]
            pixel2 = datos_pixeles2[x, y]
            #La suma 
            r = int((pixel[0] + pixel2[0])/2)
            g = int((pixel[1] + pixel2[1])/2)
            b = int((pixel[2] + pixel2[2])/2)
            pixel3 = (r,g,b)
            newImagenSuma.putpixel((x, y), pixel3)
            #La resta 
            r2 = abs((pixel[0] - pixel2[0]))
            g2 = abs((pixel[1] - pixel2[1]))
            b2 = abs((pixel[2] - pixel2[2]))
            pixel4 = (r2,g2,b2)
            newImagenResta.putpixel((x, y), pixel4)

    newImagenSuma.show()
    newImagenResta.show()