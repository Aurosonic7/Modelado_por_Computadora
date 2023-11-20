from PIL import Image
def cuadrantes(imagen,cuadrante):
    if cuadrante == 1:
        i=0
        while int(i<imagen.size[0]/2):
            j=0
            while int(j<imagen.size[1]/2):
                r,g,b = imagen.getpixel((i,j))
                suma = (r+g+b)/3
                gris = int(suma)
                pixeles = tuple([gris,gris,gris])
                imagen.putpixel((i,j),pixeles)
                j+=1
            i+=1
    elif cuadrante == 3:
        i=0
        while int(i<imagen.size[0]/2):
            j=112
            while j<imagen.size[1]:
                r,g,b = imagen.getpixel((i,j))
                suma = (r+g+b)/3
                gris = int(suma)
                pixeles = tuple([gris,gris,gris])
                imagen.putpixel((i,j),pixeles)
                j+=1
            i+=1
    elif cuadrante == 2:
        i=112
        while i<imagen.size[0]:
            j=0
            while j<int(imagen.size[1]/2):
                r,g,b = imagen.getpixel((i,j))
                suma = (r+g+b)/3
                gris = int(suma)
                pixeles = tuple([gris,gris,gris])
                imagen.putpixel((i,j),pixeles)
                j+=1
            i+=1
    elif cuadrante == 4:
        i=112
        while i<imagen.size[0]:
            j=112
            while j<imagen.size[1]:
                r,g,b = imagen.getpixel((i,j))
                suma = (r+g+b)/3
                gris = int(suma)
                pixeles = tuple([gris,gris,gris])
                imagen.putpixel((i,j),pixeles)
                j+=1
            i+=1
    imagen.show()

def volteaImg(imagen):
    fil, col = imagen.size
    newimagen = Image.new('RGB', (col, fil))
    for fila in range(fil):
        for columna in range(col):
            datos_pixeles = imagen.load()
            pixel = datos_pixeles[fila, columna]
            newimagen.putpixel((columna, fila), pixel)
    newimagen.show()

Ruta="/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 1/Actividad 3/danny.jpg"
imagen = Image.open(Ruta)
cuadrante= int(input("Digite el cuadrante(I,II,III,IV): "))
cuadrantes(imagen,cuadrante)

Ruta="/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 1/Actividad 3/danny.jpg"
imagen = Image.open(Ruta)
volteaImg(imagen)

