from PIL import Image



# Abrir la imagen
imagen = Image.open("/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 1/piramide.jpg")
imagen.show()
##Ejercicio 2

def ImagenRecortada(imagen,x1,y1,x2,y2):
    #Obtener los píxeles de la imagen
    pixeles = imagen.load()
    #Crear una nueva imagen para el recorte
    eje_x = x2 - x1
    eje_y = y2 - y1
    imagen_recortada = Image.new("RGB", (eje_x, eje_y))
    #Obtener los píxeles de la imagen recortada
    pixeles_recortados = imagen_recortada.load()
    #Copiar los píxeles del área de recorte a la nueva imagen
    for x in range(eje_x):
        for y in range(eje_y):
            pixeles_recortados[x, y] = pixeles[x1 + x, y1 + y]
    imagen_recortada.show()
# Coordenadas del área de recorte (izquierda, superior, derecha, inferior)
x1 = int(input("Digite el valor de x1: "))
y1 = int(input("Digite el valor de y1: "))
x2 = int(input("Digite el valor de x2: "))
y2 = int(input("Digite el valor de y2: "))
if x1 > x2:
    aux=x1
    x1=x2
    x2=aux
if y1 > y2:
    aux=y1
    y1=y2
    y2=aux
if y1==y2:
    y2=y2+1
if x1==x2:
    x2=x2+1

ImagenRecortada(imagen,x1,y1,x2,y2) 

##Ejercicio 4


def LineasRojasCuadradas(imagen):
    ancho, alto = imagen.size
    pixeles = imagen.load()
    for y in range(alto):
        for x in range(ancho):
            if x == y or x == ancho - y - 1:# Cambio los pixeles
                pixeles[x, y] = (255, 0, 0)  #Le asigno el color rojo
    imagen.show()
LineasRojasCuadradas(imagen)
