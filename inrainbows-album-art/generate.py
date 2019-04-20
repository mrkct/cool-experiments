from random import randint
import math
from PIL import Image, ImageDraw, ImageFont


# Did you know that calculating the correct font size
# is NP-Hard? This function is for when they will solve
# P = NP?
def calculate_font_size(string, image_width):
    global FONT_SIZE
    return FONT_SIZE

def pad_string(text, how_many):
    length = len(text)
    for _ in range(how_many):
        position = randint(1, length-1)
        text = text[:position] + ' ' + text[position:]
    return text

def generate_strings(text, how_many):
    already = [0] # because we don't like it in the first char
    strings = []
    for i in range(how_many):
        # This is to generate always different random numbers
        position = randint(0, len(text))
        if len(already) == len(text):
            already = [0]
        while position in already:
            position = randint(0, len(text))
        already.append(position)
        
        character = ['/', '_'][randint(0, 1)]
        strings.append("{}{}{}".format(
            text[:position], 
            character, 
            text[position:]
        ))
    
    return strings
        
def create_image(strings, colors, size, background):
    font_size = calculate_font_size(strings[0], size)
    line_height = 5
    image = Image.new('RGB', size)
    image.paste(background)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', font_size)
    for i in range(len(strings)):
        draw.text(
            (0, (font_size+line_height) * i), 
            strings[i], 
            fill=colors[i % len(colors)], 
            font=font
        )
    
    return image

# Size of the output image
IMAGE_SIZE = (256, 256)

# Use 34 if you want to write 'IN RAINBOWS'
FONT_SIZE = 34

# These are the colors of the original album art
COLORS = [
    (245, 230, 70),     # yellow
    (70, 138, 200),     # blue
    (237, 104, 42),     # orange
    (64, 185, 74),      # green
    (234, 173, 30),     # darker yellow
    (227, 34, 46),      # red
    (158, 222, 232)     # white/very light blue
]

main_text = "IN RAINBOWS"
lower_text = "RADIOHEAD"

if len(main_text) > len(lower_text):
    lower_text = pad_string(lower_text, len(main_text) - len(lower_text))
else:
    main_text = pad_string(main_text, len(lower_text) - len(main_text))

image = create_image(
    generate_strings(main_text, 4) + generate_strings(lower_text, 2), 
    COLORS, 
    IMAGE_SIZE,
    Image.open('background.png', mode='r')
)
image.save("output.png")