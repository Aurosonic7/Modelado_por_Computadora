from PIL import Image
imagen_rgb = Image.open("/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 1/Actividad 5/gato.jpeg")
ancho, alto = imagen_rgb.size
imagen_cmyk = Image.new("CMYK", (ancho, alto))
for y in range(alto):
    for x in range(ancho):
        pixel_rgb = imagen_rgb.getpixel((x, y))
        r, g, b = pixel_rgb
        c = 255 - r 
        m = 255 - g 
        Y = 255 - b 
        k = min(c, m, Y)
        imagen_cmyk.putpixel((x, y), (c, m, Y, k))
imagen_rgb.show()
imagen_cmyk.show()

Ruta = "/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 1/Actividad 5/gato.jpeg"
imagen = Image.open(Ruta)
ancho, alto = imagen.size
imagen_blanco = Image.new("RGB", (ancho, alto))
print("::Bienvenido al menu::")
print("1.- Rojo")
print("2.- Verde")
print("3.- Azul")
tipo = int(input("Digite una opcion: "))
mini = int(input("Ahora digite el intervalo minimo: "))
maxi = int(input("Ahora digite el intervalo maximo: "))
for fila in range(ancho):
    for columna in range(alto):
        pixel = imagen.getpixel((fila, columna))
        r, g, b = pixel          
        if tipo == 1:
            if r >= mini and r <= maxi: #Comparacion de intervalos
                r = g = b = 255 #Asignacion a los valores
        elif tipo == 2:
            if g >= mini and g <= maxi:
                r = g = b = 255
        elif tipo == 3:
            if b >= mini and b <= maxi:
                r = g = b = 255
        pixels = (r, g, b)
        imagen_blanco.putpixel((fila, columna), pixels)
imagen_blanco.show()