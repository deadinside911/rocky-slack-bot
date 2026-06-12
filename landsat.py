import os
import random

from PIL import Image


WIDTH = 1175
HEIGHT = 2817
GAP = 50

def make_landsat_image(name: str):
    name = name.upper()
    spaces = GAP * (len(name) - 1)
    landsat_image = Image.new(mode="RGB",size=(WIDTH * len(name) + spaces, HEIGHT), color="white")

    for i in range(0, len(name)):
        letter_image_name = random.choice(os.listdir(f"alphabets/{name[i]}"))
        letter_image = Image.open(f"alphabets/{name[i]}/{letter_image_name}").resize((WIDTH, HEIGHT))

        if i == 0:
            landsat_image.paste(letter_image, (i * WIDTH, 0))
        else:
            landsat_image.paste(letter_image, ((i * (WIDTH + GAP)), 0))

    
    landsat_image.save(f"{name}.png")