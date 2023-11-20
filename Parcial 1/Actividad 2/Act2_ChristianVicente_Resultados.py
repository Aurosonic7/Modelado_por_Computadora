from PIL import Image
imagen = Image.open("/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 1/Actividad 2/piedra.jpg")
ancho, alto = imagen.size
imagen_BN = Image.new("RGB", (ancho, alto))  #nueva imagen en blanco
bits= int(input("Ingresa la cantidad de bits (1,2,4,8): "))
v=0
for fila in range(ancho):
    for columna in range(alto):
        pixel = imagen.getpixel((fila, columna))
        if (bits==8):
            pixel[0]
            prom=(pixel[0],pixel[0],pixel[0])
        elif (bits==4):
            if (pixel[0]>=0 and pixel[0]<=15):
                v=0
            elif (pixel[0]>=16 and pixel[0]<=31):
                v=16
            elif (pixel[0]>=32 and pixel[0]<=47):
                v=32
            elif (pixel[0]>=48 and pixel[0]<=63):
                v=48
            elif (pixel[0]>=64 and pixel[0]<=79):
                v=64
            elif (pixel[0]>=80 and pixel[0]<=95):
                v=80
            elif (pixel[0]>=96 and pixel[0]<=111):
                v=96
            elif (pixel[0]>=112 and pixel[0]<=127):
                v=112
            elif (pixel[0]>=128 and pixel[0]<=143):
                v=128
            elif (pixel[0]>=144 and pixel[0]<=159):
                v=144
            elif (pixel[0]>=160 and pixel[0]<=175):
                v=160
            elif (pixel[0]>=176 and pixel[0]<=191):
                v=176
            elif (pixel[0]>=192 and pixel[0]<=207):
                v=192
            elif (pixel[0]>=208 and pixel[0]<=223):
                v=208
            elif (pixel[0]>=224 and pixel[0]<=239):
                v=224
            elif (pixel[0]>=240 and pixel[0]<=256):
                v=240
            prom = (v,v,v)
        elif (bits==2):
            if (pixel[0]>=0 and pixel[0]<=30):
                v=0
            elif (pixel[0]>=64 and pixel[0]<=127):
                v=64
            elif (pixel[0]>=128 and pixel[0]<=191):
                v=128
            elif (pixel[0]>=192 and pixel[0]<=256):
                v=192
            prom = (v,v,v)
        elif (bits==1):
            if (pixel[0]>=128):
                v=255
            else:
                v=0
            prom = (v,v,v)
        imagen_BN.putpixel((fila, columna), prom)  # Asigna el pixel de escala de gris en la nueva imagen
imagen_BN.show()
