from PIL import Image
import os


def resizing(factor, folder):
    if not os.path.exists(f"{folder}__{factor}"):

        os.mkdir(f"{folder}__{factor}")
        for i in os.listdir(folder):

            img = Image.open(f"{folder}/{i}")
            x, y = int(img.width // factor), int(img.height // factor)
            img = img.resize((x, y))

            img.save(f"{folder}__{factor}/{i}")
    else:
        print("file exists delete it first")


resizing(2, "elf")
resizing(2.5, "elf")
