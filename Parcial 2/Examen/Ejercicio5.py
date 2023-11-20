from PIL import Image
def gaussian_blur(image, radius):
    width, height = image.size
    pixels = image.load()
    new_image = Image.new("RGB", (width, height))
    kernel = [
        [-2,-1,0],
        [-1,1,1],
        [0,1,2]
    ]
    kernel_sum = sum(sum(row) for row in kernel)
    for x in range(width):
        for y in range(height):
            r_total, g_total, b_total = 0, 0, 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < width and 0 <= ny < height:
                        pixel = pixels[nx, ny]
                        kernel_value = kernel[dx + 1][dy + 1]
                        r_total += pixel[0] * kernel_value
                        g_total += pixel[1] * kernel_value
                        b_total += pixel[2] * kernel_value
            r = int(r_total / kernel_sum) if (kernel_sum > 0) else r_total
            g = int(g_total / kernel_sum) if (kernel_sum > 0) else g_total
            b = int(b_total / kernel_sum) if (kernel_sum > 0) else b_total
            new_pixel = (r, g, b)
            new_image.putpixel((x, y), new_pixel)
    return new_image
imagen_original = Image.open('/Users/christianvicente/Desktop/La Salle Oaxaca/5º_Semestre/Modelado para computadora/Parcial 2/Examen/chihuahua.jpg')
imagen_suavizada = gaussian_blur(imagen_original, radius=1)
imagen_original.show()
imagen_suavizada.show()