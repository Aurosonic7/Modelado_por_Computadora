from PIL import Image
def gaussian_blur(image, radius):
    width, height = image.size
    pixels = image.load()
    new_image = Image.new("RGB", (width, height))
    kernel = [
        [0, -1, 0],
        [-1, 4, -1],
        [0, -1, 0]
    ]
    kernel_sum = sum(sum(row) for row in kernel)
    for x in range(width):
        for y in range(height):
            rojo, verde, azul = 0, 0, 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < width and 0 <= ny < height:
                        pixel = pixels[nx, ny]
                        valores = kernel[dx + 1][dy + 1]
                        rojo += pixel[0] * valores
                        verde += pixel[1] * valores
                        azul += pixel[2] * valores
            r = int(rojo / kernel_sum) if (kernel_sum > 0) else rojo
            g = int(verde / kernel_sum) if (kernel_sum > 0) else verde
            b = int(azul / kernel_sum) if (kernel_sum > 0) else azul
            new_pixel = (r, g, b)
            new_image.putpixel((x, y), new_pixel)
    return new_image
imagen_original = Image.open('/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 2/Examen/chihuahua.jpg')
imagen_suavizada = gaussian_blur(imagen_original, radius=1)
imagen_original.show()
imagen_suavizada.show()