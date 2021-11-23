import scrapy
import requests
import os
import random


class DownloadImagesSpider(scrapy.Spider):
    name = 'download_images'

    def start_requests(self):
        yield scrapy.Request(url=f'https://wall.alphacoders.com/search.php?search={str(self.search).replace(" ", "+")}', callback=self.parse)
        # yield scrapy.Request(url=f'https://wall.alphacoders.com/search.php?search=re+zero', callback=self.parse)

    def parse(self, response):
        a_links = response.xpath("//div[@class='boxgrid']/a")
        for each_link in a_links:
            large_image_links = "https://wall.alphacoders.com/" + each_link.attrib["href"]
            yield scrapy.Request(url=large_image_links, callback=self.parse2)

        next_page_link = response.xpath("//a[@class='next-container']").attrib["href"]
        if next_page_link != "#":
            yield scrapy.Request(url=next_page_link, callback=self.parse)

    def parse2(self, response):
        if not os.path.exists(os.path.join(self.path, self.search)):
            os.makedirs(os.path.join(self.path, self.search))
        clean_image_url = response.xpath("//img[@class='main-content']").attrib["src"]
        r = requests.get(clean_image_url)
        with open(f"{self.path}/{self.search}/{self.search} {random.randint(1,1000000)}.jpg", "wb") as IF:
            IF.write(r.content)
