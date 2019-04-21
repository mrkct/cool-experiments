import sys
import math
from PIL import Image

def rgb_to_lightness(rgb):
    return (rgb[0] + rgb[1] + rgb[2]) / 3

def get_average_light(image, top_left, bottom_right):
    result = 0 
    total = 0
    for x in range(top_left[0], bottom_right[0]):
        for y in range(top_left[1], bottom_right[1]):
            result += rgb_to_lightness(image.getpixel((x, y)))
            total += 1
    
    return int(result / total)

def light_to_ascii(light):
    if light >= 230:
        return " "
    elif light >= 200:
        return "."
    elif light >= 180:
        return "*"
    elif light >= 160:
        return ":"
    elif light >= 130:
        return "o"
    elif light >= 100:
        return "&"
    elif light >= 70:
        return "8"
    elif light >= 50:
        return "#"
    else:
        return "@"

if len(sys.argv) < 2:
    print("Usage: img2ascii <filename> <approximation>")
    exit(0)

BLOCK_SIZE = 8
if len(sys.argv) > 2:
    BLOCK_SIZE = int(sys.argv[2])

image = Image.open(sys.argv[1])
for row in range(math.floor(image.size[1] / BLOCK_SIZE)):
    for column in range(math.floor(image.size[0] / BLOCK_SIZE)):
        lightness = get_average_light(
            image, 
            (column * BLOCK_SIZE, row * BLOCK_SIZE), 
            ((column + 1) * BLOCK_SIZE, (row + 1) * BLOCK_SIZE)
        )
        print(light_to_ascii(lightness), end="")
    print()