from PIL import Image

def RecorrerImagen():
    Ruta = "kick.jpeg"
    imagen1 = Image.open(Ruta)
    ancho, alto = imagen1.size
    for fila in range(ancho):
        for columna in range(alto):
            pixel = imagen1.getpixel((columna, fila))
            print("fila:", fila, "columna", columna, "=", pixel)

def LeerImagen():
    Ruta = "/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 1/Actividad 1/kick.jpeg"
    imagen1 = Image.open(Ruta)
    imagen1.show()

def ImagenGris():
    Ruta = "/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 1/Actividad 1/kick.jpeg"
    imagen1 = Image.open(Ruta)
    i = 0
    while i< imagen1.size[0]:
        j = 0
        while j<imagen1.size[1]:
            r,g,b = imagen1.getpixel((i,j))
            suma = (r+g+b)/3
            gris = int(suma)
            pixeles = tuple([gris,gris,gris])
            imagen1.putpixel((i,j),pixeles)
            j+=1
        i+=1
    imagen1.show()

def ImagenNegro(escala):
    Ruta = "/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 1/Actividad 1/kick.jpeg"
    imagen1 = Image.open(Ruta)
    i = 0
    while i< imagen1.size[0]:
        j = 0
        while j<imagen1.size[1]:
            r,g,b = imagen1.getpixel((i,j))
            suma = (r+g+b)/3
            gris = int(suma)
            if gris < escala:
                imagen1.putpixel((i,j),(0,0,0))
            else:
                imagen1.putpixel((i,j),(255,255,255))
            j+=1
        i+=1
    imagen1.show()

LeerImagen()
ImagenGris()
ImagenNegro(80)