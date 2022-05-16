import requests
from bs4 import BeautifulSoup
from random import randint
import os


def download(search, pages=1000000):
    os.mkdir(f"images_of {search}")
    rs = requests.get(f"https://wall.alphacoders.com/search.php?search={search.replace(' ', '+')}").text
    soup = BeautifulSoup(rs, "lxml")
    match = soup.find_all("div", class_="boxgrid")
    next_page_link = soup.find("a", class_="next-container")["href"]
    current_page = 1
    while current_page <= pages and next_page_link != "#":
        for i in match:
            large_image_html = requests.get(f'https://wall.alphacoders.com/{i.a["href"]}').text
            soup2 = BeautifulSoup(large_image_html, "lxml")
            real_image_link = soup2.find("img", class_="main-content")["src"]
            content_of_real_image_link = requests.get(real_image_link)
            with open(f"images_of {search}/{search} page{current_page} {randint(1, 10000000)}.jpg", "wb") as image_file:
                image_file.write(content_of_real_image_link.content)
        current_page += 1
        next_page_link = soup.find("a", class_="next-container")["href"]
        rs = requests.get(next_page_link).content
        soup = BeautifulSoup(rs, "lxml")
        match = soup.find_all("div", class_="boxgrid")

    return True
download("emma stone", pages=3)
