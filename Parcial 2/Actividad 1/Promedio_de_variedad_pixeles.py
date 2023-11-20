from PIL import Image

Ruta = "/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 2/Actividad 1/images.jpeg";

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

tamano_vecindad = (3, 3)

resultado = Image.new(imagen1.mode, imagen1.size)

ancho, alto = imagen1.size

for y in range(alto):
    for x in range(ancho):
        y_inicio = max(0, y - tamano_vecindad[1] // 2)
        y_fin = min(alto, y + tamano_vecindad[1] // 2 + 1)
        x_inicio = max(0, x - tamano_vecindad[0] // 2)
        x_fin = min(ancho, x + tamano_vecindad[0] // 2 + 1)

        area = [imagen1.getpixel((x, y)) for y in range(y_inicio, y_fin) for x in range(x_inicio, x_fin)]

        rango = tuple(int(sum(canal) / len(area)) for canal in zip(*area))

        resultado.putpixel((x, y), rango)

print('IMAGEN RESULTADO')
for fila in range(225):
    for columna in range(225):
        pixel = resultado.getpixel((columna, fila))
        if fila == 150:
            print("fila:", fila, "columna", columna, "=", pixel)
print("\n")
print('IMAGEN ORIGINAL')
for fila in range(225):
    for columna in range(225):
        pixel = imagen1.getpixel((columna, fila))
        if fila == 150:
            print("fila:", fila, "columna", columna, "=", pixel)

resultado.show()