from PIL import Image

def gaussian_blur(image, radius):
    width, height = image.size
    pixels = image.load()
    new_image = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            r_total, g_total, b_total, count = 0, 0, 0, 0
            for dx in range(-radius, radius + 1):
                for dy in range(-radius, radius + 1):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < width and 0 <= ny < height:
                        r, g, b = pixels[nx, ny]
                        r_total += r
                        g_total += g
                        b_total += b
                        count += 1
            new_pixel = (r_total // count, g_total // count, b_total // count)
            new_image.putpixel((x, y), new_pixel)

    return new_image
imagen_original = Image.open('/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 2/Examen/chihuahua.jpg')
imagen_difuminada = gaussian_blur(imagen_original, radius=3)
imagen_original.show()
imagen_difuminada.show()