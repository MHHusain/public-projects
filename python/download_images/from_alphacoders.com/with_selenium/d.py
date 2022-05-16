import requests
import os
import random
text_files = os.listdir(r"C:\Users\NS\Desktop\anime images project\text_files")
for text_file in text_files:
    os.mkdir(f'images_of {text_file}')
    with open(f"C:/Users/NS/Desktop/anime images project/text_files/{text_file}") as text:
        links = text.read().split('\n')
        for each_link in links:
            try:
                image = requests.get(each_link)

                with open(f'images_of {text_file}/{random.random()}.jpg', 'wb') as image_file:
                    image_file.write(image.content)
            except requests.exceptions.MissingSchema:
                pass
